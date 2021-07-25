import psycopg2
import os

host = os.getenv("DB_HOST", "localhost")
database = os.getenv("DB_DATABASE_NAME", "mydatabase")
password = os.getenv("DB_PASSWORD", "changeme")
port = os.getenv("DB_PORT", 5432)

port = int(port)

conn = psycopg2.connect(
    host=host, database=database, user="postgres", password=password, port=port
)

if conn:
    print("Connected OK")
