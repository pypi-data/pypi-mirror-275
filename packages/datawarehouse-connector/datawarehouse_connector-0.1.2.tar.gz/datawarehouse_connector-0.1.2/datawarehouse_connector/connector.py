import os
os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib
from sqlalchemy.engine.url import URL

from datawarehouse_connector.constants import *


def get_session(data):
     
    db_source = data.get(DB_SOURCE)
    username = data.get(USERNAME)
    host = data.get(HOST)
    password = data.get(PASSWORD)
    role = data.get(ROLE)
    warehouse = data.get(WAREHOUSE)
    database = data.get(DATABASE)

    db_connection_string = ""
    try:
        if db_source == SNOWFLAKE:
            encoded_password = urllib.parse.quote(password, safe="")
            db_connection_string = f"{SNOWFLAKE}://{username}:{encoded_password}@{host}/{data}/{database}?{WAREHOUSE}={warehouse}&{ROLE}={role}"
            version_query = "SELECT CURRENT_VERSION()"
        elif db_source == REDSHIFT:
            db_connection_string = URL.create(
                drivername=REDSHIFT_DRIVER_KEY,
                host=host,
                port=5439,
                database=database,
                username=username,
                password=password,
            )
            version_query = "SELECT version()"
        elif db_source == POSTGRESQL:
            db_connection_string = f"{POSTGRESQL}+{PSYCOPG2_KEY}://{username}:{password}@{host}:{5432}/{database}"
            version_query = "SELECT version()"
        else:
            print("DataSource not supported at the moment...")
            return None

        engine = create_engine(db_connection_string)
        Session = sessionmaker(bind=engine)
        session = Session()

        if session:
            # Test the connection
            result = session.execute(version_query).fetchone()
            print(f"{db_source} version: {result[0]}")
            return session
        else:
            return None
    except Exception as e:
        print(str(e))
