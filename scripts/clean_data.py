import pandas as pd
from sqlalchemy import create_engine

#minio giris
storage_options = {"key": "minioadmin", "secret": "minioadmin", "client_kwargs": {"endpoint_url": "http://minio:9000"}}
df = pd.read_csv("s3://dataops-bronze/raw/dirty_store_transactions.csv", storage_options=storage_options)

#drop
df = df.drop_duplicates() 
df = df.dropna()          
# sayısal olmayanları temizle

#
engine = create_engine('postgresql://trainuser:trainpassword@postgres:5432/traindb')
df.to_sql('clean_data_transactions', engine, if_exists='replace', index=False)

print("veri temizlendi, postgresql'e yuklendi")

