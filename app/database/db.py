import psycopg2
from psycopg2 import DatabaseError
from decouple import config
 
def get_connection():
     try:
         return psycopg2.connect(
             dbname=config('DB_NAME'),
             user=config('DB_USER'),
             password=config('DB_PASSWORD'),
             host=config('DB_HOST'),
             port=config('DB_PORT')
         )
     except DatabaseError as ex:
         raise ex