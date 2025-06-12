import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection_mysql():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
