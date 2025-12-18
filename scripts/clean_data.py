import pandas as pd
from sqlalchemy import create_engine

# 1. MinIO'dan Oku
storage_options = {
    "key": "minioadmin",
    "secret": "minioadmin",
    "client_kwargs": {"endpoint_url": "http://minio:9000"}
}

print("MinIO'dan veri okunuyor...")
df = pd.read_csv("s3://dataops-bronze/raw/dirty_store_transactions.csv", storage_options=storage_options)

# 2. Veri Temizleme (Assignment Requirements)
print("Veri temizleniyor...")
df = df.drop_duplicates()  # Tekrar eden kayıtları sil
df = df.dropna()           # Eksik verileri (NaN) sil

# 3. PostgreSQL'e Yaz (Data Sink)
print("PostgreSQL'e yazılıyor...")
# Kullanıcı: admin, Şifre: (Docker'da neyse, genelde admin veya trainpassword)
# Host: postgres (Docker network ismi)
# DB: traindb
engine = create_engine('postgresql://admin:admin@postgres:5432/traindb')

# Tablo adı: clean_data_transactions
df.to_sql('clean_data_transactions', engine, if_exists='replace', index=False)

print("Başarıyla tamamlandı: Veri temizlendi ve PostgreSQL'e yazıldı!")
