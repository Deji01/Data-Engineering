import glob
from process_data import transform
from goat.sql_query import create_table_query, insert_data_query
from utils.postgres_db import create_connection, create_table, store_db


def load():
    # create database connection
    connection, curr = create_connection()

    # create table if it doesn't exist
    create_table(curr, create_table_query)

    # read in json files in data dir
    files = glob.glob("./data/*.json")

    for file in files:
        # get data from file
        items = transform(file)

        for value in items:
            # store data in database
            store_db(curr, insert_data_query, value)
            connection.commit()

    # close cursor and connection
    curr.close()
    connection.close()


if __name__ == "__main__":
    load()
