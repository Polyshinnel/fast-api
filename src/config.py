from dotenv import load_dotenv
import os

load_dotenv()

DB_DRIVER = os.environ.get('DB_DRIVER')
DB_NAME = os.environ.get('DB_NAME')
