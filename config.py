import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PATH_TO_DB = os.path.join(DATA_DIR, "receipts_database.db")
PATH_TO_USER_DB = os.path.join(DATA_DIR, "user.db")
