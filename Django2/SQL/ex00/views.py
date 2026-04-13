from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from d06.utils import load_query, get_sql_path
import psycopg2


# Create your views here.
def init(request):
    # Get database setting from d06/settings.py
    db = settings.DATABASES['default']

    conn = None
    try:
        # Establishing connection using psycopg2
        conn = psycopg2.connect(
            dbname = db['NAME'],
            user = db['USER'],
            password = db['PASSWORD'],
            host = db['HOST'],
            port = db['PORT']
        )

        # We Create a cursor instance to execute SQL
        cur = conn.cursor()

        # Define the table creation query
        query = load_query(get_sql_path('ex00', 'schema.sql'))

        cur.execute(query)

        # Commit the changes to the database
        conn.commit()

        # Close communication
        cur.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

    finally:
        # Ensure the connection is closed even if an error occurs
        if conn is not None:
            conn.close()


