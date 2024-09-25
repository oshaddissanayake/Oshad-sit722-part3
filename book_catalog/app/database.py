from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://oshad_sit722_part3_user:VjmxlIGd4sH9YLPO5eJdhJqfMXjyKL0M@dpg-crj88ju8ii6s73fddctg-a.oregon-postgres.render.com/oshad_sit722_part3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
