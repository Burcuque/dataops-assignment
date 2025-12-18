import pandas as pd
from sqlalchemy import create_engine

#
storage_options = {
    "key": "minioadmin",
    "secret": "minioadmin",
    "client_kwargs": {"endpoint_url": "http://minio:9000"}
}
# s3fs kullanarak oku
df = pd.read_csv("s3://dataops-bronze/raw/dirty_store_transactions.csv", storage_options=storage_options)

#
df = df.drop_duplicates()  
df = df.dropna()           #


engine = create_engine('postgresql://admin:admin@postgres:5432/traindb')

df.to_sql('clean_data_transactions', engine, if_exists='replace', index=False)

print("veri temizlendi ve DB'ye yazıldı.")
