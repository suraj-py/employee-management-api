from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

# create postgresql database instance
engine = create_engine(DATABASE_URL)

# create session local class for session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create declarative base meta instance
Base = declarative_base()

