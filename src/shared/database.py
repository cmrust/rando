from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

path_to_sqllite = "./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{path_to_sqllite}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# connect_args check_same_thread are for sqllite only
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# create database session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class of database models
Base = declarative_base()