import os
import pandas as pd
import ants

from tempfile import NamedTemporaryFile
from google.cloud import storage
from google.oauth2 import service_account

class ColumnReader:
    def __init__(self, column, base_file=None, is_image=False, label=None):
        """
        Examples
        --------
        >>> import numpy as np
        >>> from tempfile import NamedTemporaryFile
        >>> import pandas as pd
        >>> from nitrain.readers import ColumnReader
        >>> df = pd.DataFrame.from_dict({'x':[1,2,3], 'y':['a','b','c']})
        >>> file = NamedTemporaryFile(suffix='.csv')
        >>> df.to_csv(file.name)
        >>> reader = ColumnReader(file.name, 'x')
        >>> value = reader[1] # 'b'
        """
        self.base_file = base_file
        self.column = column
        self.is_image = is_image
        self.label = label

    def select(self, idx):
        new_reader = ColumnReader(self.column, self.base_file, self.is_image, self.label)
        new_reader.values = self.values
        new_reader.values = [new_reader.values[i] for i in idx]
        return new_reader
        
    def map_gcs_values(self, bucket, credentials, base_dir=None, base_file=None, base_label=None):
        file = self.base_file
        if file is None:
            if base_file is None:
                raise Exception('You must either supply `file` to ColumnReader or `base_file` to Dataset')
            file = base_file
            base_dir = None # dont look at base_dir if base_file is supplied
            
        column = self.column
        is_image = self.is_image

        if base_dir is not None:
            file = os.path.join(base_dir, file)

        # GCS
        if isinstance(credentials, str):
            credentials = service_account.Credentials.from_service_account_file(credentials)
        storage_client = storage.Client(credentials=credentials)
        bucket_client = storage_client.bucket(bucket)
        
        ## read file
        tmp_file = NamedTemporaryFile(suffix=os.path.splitext(file)[-1])
        blob = bucket_client.blob(file)
        blob.download_to_filename(tmp_file.name)
        
        if file.endswith('.tsv'):
            participants = pd.read_csv(tmp_file.name, sep='\t')
        elif file.endswith('.csv'):
            participants = pd.read_csv(tmp_file.name)
            
        values = participants[column].to_numpy()
        
        self.values = values
        self.file = file
        self.column = column
        self.is_image = is_image
        
        if self.label is None:
            if base_label is not None:
                self.label = base_label
            else:
                self.label = 'column'
        
    def map_values(self, base_dir=None, base_file=None, base_label=None):
        file = self.base_file
        if file is None:
            if base_file is None:
                raise Exception('You must either supply `file` to ColumnReader or `base_file` to Dataset')
            file = base_file
            base_dir = None # dont look at base_dir if base_file is supplied
            
        column = self.column
        is_image = self.is_image

        if base_dir is not None:
            file = os.path.join(base_dir, file)
        
        file = os.path.expanduser(file)
        if not os.path.exists(file):
            raise Exception(f'No file found at {file}')
        
        if file.endswith('.tsv'):
            participants = pd.read_csv(file, sep='\t')
        elif file.endswith('.csv'):
            participants = pd.read_csv(file)
            
        values = participants[column].to_numpy()
        
        self.values = list(values)
        self.file = file
        self.column = column
        self.is_image = is_image
        
        if self.label is None:
            if base_label is not None:
                self.label = base_label
            else:
                self.label = 'column'

    def __getitem__(self, idx):
        value = self.values[idx]
        if self.is_image:
            value = ants.image_read(value)
        return {self.label: value}

    def __len__(self):
        return len(self.values)