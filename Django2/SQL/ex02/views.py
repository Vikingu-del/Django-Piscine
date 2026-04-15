from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from d06.utils import load_query, get_sql_path
import psycopg2


def connect_db(database='default'):
    db = settings.DATABASES[database]
    return psycopg2.connect(
        dbname = db['NAME'],
        user = db['USER'],
        password = db['PASSWORD'],
        host = db['HOST'],
        port = db['PORT']
    )


def execute_query(query, database='default', type='commit'):
    conn = None
    try:
        conn = connect_db(database)
        if type == 'fetch':
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        else:
            cur = conn.cursor()
        cur.execute(query)
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


# Create your views here.
def init(request):
    query = load_query(get_sql_path('ex02', 'schema.sql'))
    try:
        execute_query(query, type='commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def populate(request):
    query = load_query(get_sql_path('ex02', 'populate.sql'))
    try:
        execute_query(query, type='commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))
    

def display(request):
    query = load_query(get_sql_path('ex02', 'fetch.sql'))
    try:
        data = execute_query(query, type='fetch')
        print(data)
        return render(request, 'ex02/display.html', {'movies': data})
    except Exception as e:
        return HttpResponse(str(e))
