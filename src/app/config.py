import os

USERNAME = ''
PASSWORD = ''

BASE_DIR = os.path.dirname(__file__)
SQL_ROOT_PATH = os.path.join(BASE_DIR, 'sql')
CHROME_PROFILE_PATH = os.environ.get('CHROME_PROFILE_PATH')
DATABASE = {
    "dbname": os.environ["POSTGRES_DB"],
    "user": os.environ["POSTGRES_USER"],
    "host": os.environ["POSTGRES_HOST"],
    "password": os.environ["POSTGRES_PASSWORD"]
}