from psycopg2 import connect
from psycopg2._psycopg import OperationalError
import os

def create_connection():
    try:
        conn = connect(
            host= 'database-2.chigbhalevl1.us-east-2.rds.amazonaws.com',
            database= 'postgres',
            user='areesh',
            password='Yg5*43rc',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(e)


connection = create_connection()
