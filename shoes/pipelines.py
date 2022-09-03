# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from shoes.config import db_host, db_name, db_password, db_port, db_user
from itemadapter import ItemAdapter
import psycopg2
import sys


class ShoesPipeline:
    def process_item(self, item, spider):
        return item


class SaveToPostgreSQLPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
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
            self.connection = psycopg2.connect(conn_string)
            print("Connection established")

        except psycopg2.Error as e:
            print(f"Error connecting to Postgres DB : {e}")
            sys.exit(1)

        self.curr = self.connection.cursor()

    def create_table(self):
        "Create Table in Database if it does not exist"

        self.curr.execute(
            """
            CREATE TABLE IF NOT EXISTS sole_supplier (
                date TIMESTAMPTZ NOT NULL DEFAULT NOW(), 
                style_code VARCHAR(15),
                product_title VARCHAR(255), 
                stock_status VARCHAR(20), 
                release_date VARCHAR(30), 
                price NUMERIC(10, 2), 
                brand VARCHAR(20), 
                model VARCHAR(20),  
                image_url VARCHAR(255) NOT NULL PRIMARY KEY
            )
            """
        )

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        "Insert data into Database and commit changes"

        query = """
                INSERT INTO sole_supplier (style_code, product_title, stock_status, release_date, price, brand, model, image_url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
        value = (
            item.get("style_code"),
            item.get("product_title"),
            item.get("stock_status"),
            item.get("release_date"),
            item.get("price"),
            item.get("brand"),
            item.get("model"),
            item.get("image_url"),
        )
        try:
            self.curr.execute(query, value)

        except BaseException as e:
            print(e)

        self.connection.commit()

    def close_spider(self, spider):
        try:
            self.curr.execute(
                """
                    UPDATE sole_supplier 
                    SET style_code = model , model = style_code
                    WHERE model <> %s AND model ~ %s AND style_code is NULL;
                    """,
                ("Dunk", "^[a-zA-Z]{2,3}[0-9]{3,4}[-][0-9]{3,4}$"),
            )
        except BaseException as e:
            print(f"swap style code and model (1) : {e}")

        try:
            self.curr.execute(
                """
                    UPDATE sole_supplier 
                    SET style_code = model , model = style_code
                    WHERE model <> %s AND model ~ %s AND style_code is NULL;
                    """,
                ("Dunk", "^[0-9]{6}[-][0-9]{3,4}$"),
            )
        except BaseException as e:
            print(f"swap style code and model (2) : {e}")

        try:
            self.curr.execute(
                """
                    UPDATE sole_supplier 
                    SET brand = %s , model = %s
                    WHERE brand = %s;
                    """,
                ("Nike", "Dunk", "Dunk"),
            )
        except BaseException as e:
            print(f"Update Nike - Dunk : {e}")

        try:
            self.curr.execute(
                """
                    DELETE FROM sole_supplier
                    WHERE brand <> %s;
                    """,
                ("Nike"),
            )
        except BaseException as e:
            print(f"Delete other brands : {e}")

        try:
            self.curr.execute(
                """
                    DELETE FROM sole_supplier
                    WHERE price IS NULL;
                    """
            )
        except BaseException as e:
            print(f"Delete products without price : {e}")

        self.connection.commit()
        
        self.curr.close()
        self.connection.close()
