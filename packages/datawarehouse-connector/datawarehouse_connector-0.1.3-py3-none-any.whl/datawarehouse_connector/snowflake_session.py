import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datawarehouse_connector.constants import *
from datawarehouse_connector.utils import logger

class SnowflakeSession:
    def __init__(self, data):
        self.data = data

    def create_session(self):
        try:
            username = self.data.get(USERNAME)
            host = self.data.get(HOST)
            password = self.data.get(PASSWORD)
            role = self.data.get(ROLE)
            warehouse = self.data.get(WAREHOUSE)
            database = self.data.get(DATABASE)
            encoded_password = urllib.parse.quote(password, safe="")
            db_connection_string = (
                f"snowflake://{username}:{encoded_password}@{host}/{database}"
                f"?warehouse={warehouse}&role={role}"
            )
            engine = create_engine(db_connection_string)
            Session = sessionmaker(bind=engine)
            session = Session()
            if session:
                result = session.execute("SELECT CURRENT_VERSION()").fetchone()
                logger.info(f"Snowflake version: {result[0]}")
                return session
        except Exception as e:
            logger.exception(RED + " Failed to create Snowflake session " + ENDC)
            return None
