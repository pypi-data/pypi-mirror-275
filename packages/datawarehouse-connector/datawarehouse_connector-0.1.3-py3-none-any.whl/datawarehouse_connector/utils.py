import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
# Suppress SQLAlchemy debug messages
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Set environment variables
os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'
