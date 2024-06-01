import psycopg2
from psycopg2 import DatabaseError
from decouple import config
 
def get_connection():
    try:
        return psycopg2.connect(
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            host=config('PGSQL_HOST'),
            port=config('PGSQL_PORT')
        )
    except DatabaseError as ex:
        raise ex