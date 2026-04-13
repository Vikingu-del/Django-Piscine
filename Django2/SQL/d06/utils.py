import os

def load_query(filename: str) -> str:
    """ Utility Funtion to load an sql file """
    with open(filename, 'r') as f:
        return f.read()

def get_sql_path(app_name, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, app_name, filename)
