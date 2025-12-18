import pandas as pd
from sqlalchemy import create_engine

# 1. MinIO'dan oku (S3 protokolü ile)
df = pd.read_csv("http://minio:9000/dataops-bronze/raw/dirty_store_transactions.csv")

# 2. Temizle
df = df.drop_duplicates().dropna()

# 3. PostgreSQL'e yaz
engine = create_engine('postgresql://user:pass@postgres:5432/traindb')
df.to_sql('clean_data_transactions', engine, if_exists='replace', index=False)
