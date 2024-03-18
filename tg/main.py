import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, type_p):
        database = db.connect(
            database="n37",
            user="postgres",
            host="localhost",
            password="2004"

        )
        cursor = database.cursor()
        cursor.execute(query)

        data = ["insert", "create"]
        if type_p in data:
            if type_p == " insert":
                database.commit()
                return " Inserted"

        else:
            return cursor.fetchall()
