from .config import db_host, db_name, db_password, db_user
import psycopg2
import sys


def create_connection():
    "Create Database Connection"

    host = db_host
    dbname = db_name
    user = db_user
    password = db_password
    sslmode = "require"

    # Constructing connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
        host, user, dbname, password, sslmode
    )

    try:
        connection = psycopg2.connect(conn_string)
        print("Connection established")

    except psycopg2.Error as e:
        print(f"Error connecting to Postgres DB : {e}")
        sys.exit(1)

    curr = connection.cursor()
    return connection, curr


def create_table(curr, query):
    "Create Table in Database if it does not exist"
    try:
        curr.execute(query)

    except BaseException as e:
        print(e)


def store_db(curr, query, value):
    "Insert data into Database and commit changes"
    try:
        curr.execute(query, value)

    except BaseException as e:
        print(e)

