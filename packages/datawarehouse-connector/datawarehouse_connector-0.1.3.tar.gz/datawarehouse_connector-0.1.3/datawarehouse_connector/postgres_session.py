from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datawarehouse_connector.constants import *
from datawarehouse_connector.utils import logger

class PostgresSession:
    def __init__(self, data):
        self.data = data

    def create_session(self):
        try:
            username = self.data.get(USERNAME)
            host = self.data.get(HOST)
            password = self.data.get(PASSWORD)
            database = self.data.get(DATABASE)
            db_connection_string = (
                f"postgresql+{PSYCOPG2_KEY}://{username}:{password}@{host}:5432/{database}"
            )
            engine = create_engine(db_connection_string)
            Session = sessionmaker(bind=engine)
            session = Session()
            if session:
                result = session.execute("SELECT version()").fetchone()
                logger.info(f"PostgreSQL version: {result[0]}")
                return session
        except Exception as e:
            logger.exception(RED + " Failed to create PostgreSQL session " + ENDC)
            return None
