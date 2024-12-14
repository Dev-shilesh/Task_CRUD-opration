import pymysql 
import os 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# CREATE DATABASE
def create_database():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
        conn.close()
        print(f"{DB_NAME}Database created successfully")
    except Exception as e:
        print(e)
    

def config_db(app):
    try:
        app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        # Debug purpose log details
        # app.config["SQLALCHEMY_ECHO"] = True

        db = SQLAlchemy(app)
        print("SQLAlchemy initialized successfully")
        return db
    
    except Exception as e:
        print(e)
    



