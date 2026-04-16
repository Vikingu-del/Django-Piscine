import os
import psycopg2
from .settings import DATABASES

def connect_db(database='default'):
    db = DATABASES[database]
    return psycopg2.connect(
        dbname = db['NAME'],
        user = db['USER'],
        password = db['PASSWORD'],
        host = db['HOST'],
        port = db['PORT']
    )

def execute_query(query, params=None, database='default', type='commit'):
    conn = None
    try:
        conn = connect_db(database)
        if type == 'fetch':
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        else:
            cur = conn.cursor()
        cur.execute(query, params)
        if type == 'fetch':
            result = cur.fetchall()
        elif type == 'commit':
            result = conn.commit()
        cur.close()
        return result
    except Exception as e:
        raise e
    finally:
        if conn is not None:
            conn.close()


def load_query(filename: str) -> str:
    """ Utility Funtion to load an sql file """
    with open(filename, 'r') as f:
        return f.read()

def get_sql_path(app_name, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, app_name, filename)
