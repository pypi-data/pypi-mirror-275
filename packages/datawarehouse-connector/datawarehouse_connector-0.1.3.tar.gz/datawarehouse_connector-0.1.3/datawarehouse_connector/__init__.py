import os
import urllib
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from datawarehouse_connector.constants import *
from datawarehouse_connector.connector import DatabaseSessionFactory

# logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)