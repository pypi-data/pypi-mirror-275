from datawarehouse_connector.constants import *
from datawarehouse_connector.snowflake_session import SnowflakeSession
from datawarehouse_connector.redshift_session import RedshiftSession
from datawarehouse_connector.postgres_session import PostgresSession
from datawarehouse_connector.utils import logger

# Factory Pattern Implementation
class DatabaseSessionFactory:
    def __init__(self, data):
        self.data = data

    def get_session(self):
        db_source = self.data.get(DB_SOURCE)
        if db_source == SNOWFLAKE:
            return SnowflakeSession(self.data).create_session()
        elif db_source == REDSHIFT:
            return RedshiftSession(self.data).create_session()
        elif db_source == POSTGRESQL:
            return PostgresSession(self.data).create_session()
        else:
            logger.error(RED + " DataSource " + self.data.get(DB_SOURCE) + " not supported at the moment... " + ENDC)
            return None
