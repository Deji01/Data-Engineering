from utils.postgres_db import create_connection

def clean_data(connection, curr):
    try:
        curr.execute(
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
        curr.execute(
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
        curr.execute(
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
        curr.execute(
            """
                DELETE FROM sole_supplier
                WHERE brand <> %s;
                """,
            ("Nike"),
        )
    except BaseException as e:
        print(f"Delete other brands : {e}")

    try:
        curr.execute(
            """
                DELETE FROM sole_supplier
                WHERE price IS NULL;
                """
        )
    except BaseException as e:
        print(f"Delete products without price : {e}")

    connection.commit()
    curr.close()
    connection.close()


if __name__ == "__main__":
    # create database connection
    connection, curr = create_connection()

    # clean database
    clean_data(connection, curr)