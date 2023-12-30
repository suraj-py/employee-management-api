from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}"

# create postgresql database instance
engine = create_engine(DATABASE_URL)

# create session local class for session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create declarative base meta instance
Base = declarative_base()

