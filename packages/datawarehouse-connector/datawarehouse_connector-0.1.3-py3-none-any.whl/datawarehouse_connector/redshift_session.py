import paramiko
from io import StringIO
import time
import threading
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from datawarehouse_connector.constants import *
from datawarehouse_connector.utils import logger

keep_tunnel_event = True
class RedshiftSession:
    def __init__(self, data):
        self.data = data
        self.ssh_tunnel = None

    def create_ssh_tunnel(self):
        try:
            ssh_host = self.data.get(SSH_HOST)
            ssh_username = self.data.get(SSH_USERNAME)
            ssh_pem_file_content = self.data.get(SSH_PEM_FILE_CONTENT)
            redshift_host = self.data.get(HOST)
            redshift_port = 5439  # Redshift default port
            ssh_private_key = (
                paramiko.RSAKey(file_obj=StringIO(ssh_pem_file_content))
                if ssh_pem_file_content and ssh_pem_file_content != ""
                else None
            )
            with SSHTunnelForwarder(
                (ssh_host, 22),
                ssh_username=ssh_username,
                ssh_pkey=ssh_private_key,
                remote_bind_address=(redshift_host, int(redshift_port)),
                local_bind_address=(LOCALHOST, 5439),  # Use the same local port
            ) as ssh_tunnel:
                logger.info(YELLOW + " SSH tunnel established" + ENDC)
                global keep_tunnel_event
                while keep_tunnel_event:
                    time.sleep(1)
                else:
                    ssh_tunnel.stop()
                    print("stopped ssh_tunnel")
            logger.info("SSH tunnel established")
        except Exception as e:
            logger.exception(RED + " Failed to create SSH tunnel " + ENDC)
            raise

    def start_ssh_tunnel(self):
        ssh_thread = threading.Thread(target=self.create_ssh_tunnel)
        ssh_thread.daemon = True
        ssh_thread.start()
        
    def create_session(self):
        try:
            host = self.data.get(HOST)
            ssh_tunnel_connection = self.data.get('ssh_tunnel_connection')
            if ssh_tunnel_connection:
                if SSH_HOST in self.data and SSH_USERNAME in self.data and SSH_PEM_FILE_CONTENT in self.data:
                    self.start_ssh_tunnel()
                    time.sleep(5)
                    host = LOCALHOST
                else:
                    if SSH_HOST not in self.data:
                        print(SSH_HOST +' '+ MISSING_MSG)
                    elif SSH_USERNAME not in self.data:
                        print(SSH_USERNAME +' '+ MISSING_MSG)
                    elif SSH_PEM_FILE_CONTENT not in self.data:
                        print(SSH_PEM_FILE_CONTENT +' '+ MISSING_MSG)

            username = self.data.get(USERNAME)
            password = self.data.get(PASSWORD)
            database = self.data.get(DATABASE)
            db_connection_string = URL.create(
                drivername=REDSHIFT_DRIVER_KEY,
                host=host,
                port=5439,
                database=database,
                username=username,
                password=password,
                query={'sslmode': 'verify-ca'}  # Adjust sslmode as needed
            )
            engine = create_engine(db_connection_string)
            Session = sessionmaker(bind=engine)
            session = Session()
            if session:
                result = session.execute("SELECT version()").fetchone()
                logger.info(f"Redshift version: {result[0]}")
                return session
        except Exception as e:
            logger.exception(RED + " Failed to create Redshift session " + ENDC)
            return None
        finally:
            if self.ssh_tunnel:
                self.ssh_tunnel.stop()
                logger.info("SSH tunnel closed")

    def stop_ssh_tunnel(self):
        if self.ssh_tunnel:
            self.ssh_tunnel.stop()
            logger.info("SSH tunnel closed")