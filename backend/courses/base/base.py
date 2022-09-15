# coding=utf-8
import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv('POSTGRES_CONNECTION_STRING'))
Session = sessionmaker(bind=engine)

Base = declarative_base()