import os
import psycopg2
from .settings import DATABASES, BASE_DIR


def connect_db(database="default"):
    db = DATABASES[database]
    return psycopg2.connect(
        dbname=db["NAME"],
        user=db["USER"],
        password=db["PASSWORD"],
        host=db["HOST"],
        port=db["PORT"],
    )


def execute_query(query, params=None, database="default", type="commit"):
    conn = None
    try:
        conn = connect_db(database)
        if type == "fetch":
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        else:
            cur = conn.cursor()
        cur.execute(query, params)
        if type == "fetch":
            result = cur.fetchall()
        elif type == "commit":
            result = conn.commit()
        cur.close()
        return result
    except Exception as e:
        raise e
    finally:
        if conn is not None:
            conn.close()


def load_query(filename: str) -> str:
    """Utility Funtion to load an sql file"""
    with open(filename) as f:
        return f.read()


def get_sql_path(app_name, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, app_name, filename)


def copy_from_csv_to_db(
    app_name: str, table_configs: dict, database: str = "default"
) -> list:
    """
    table_configs: { 'table_name': ('col1', 'col2', 'file.csv') }
    """
    results = []
    conn = None
    cur = None
    try:
        conn = connect_db(database)
        cur = conn.cursor()
        for table_name, config in table_configs.items():
            # Destructure the tuple: (column_names_tuple, filename)
            columns, file_name = config
            csv_path = os.path.join(BASE_DIR, app_name, file_name)

            with open(csv_path) as f:
                cur.copy_from(f, table_name, sep="\t", null="NULL", columns=columns)
            results.append(f"OK: file: {file_name} uploaded to table {table_name}")

        conn.commit()
        return results
    except Exception as e:
        if conn:
            conn.rollback()
        return [f"Error: {e}"]
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
