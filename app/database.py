from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://suraj:suraj1234pdb@localhost/emp_api"

# create postgresql database instance
engine = create_engine(DATABASE_URL)

# create session local class for session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create declarative base meta instance
Base = declarative_base()

