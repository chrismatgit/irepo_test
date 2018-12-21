import psycopg2
import psycopg2.extras
from pprint import pprint
import os

class DatabaseConnection:
    def __init__(self):
        if os.getenv('DB_NAME') == 'ireport_db':
            self.db_name = 'ireport_db'
        else:
            self.db_name = 'ddvageejepfvgp'

        try:
            self.connection = psycopg2.connect(dbname='ddvageejepfvgp', user='fjqrdfbxlzupju', host='ec2-174-129-25-182.compute-1.amazonaws.com', password='ef61d817399f1beacee358af0e58a8b6f1b6e913ca1a7936214d0a93d31b4de8', port =5432)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            pprint('Connected to the database successfully')

            create_user_table = "CREATE TABLE IF NOT EXISTS users (user_id SERIAL NOT NULL PRIMARY KEY,firstname TEXT NOT NULL, lastname TEXT NOT NULL, othernames TEXT NOT NULL, email TEXT NOT NULL, phone_number TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, registered TEXT NOT NULL, isadmin BOOL DEFAULT FALSE);"
            self.cursor.execute(create_user_table)

            create_incident_table = "CREATE TABLE IF NOT EXISTS incidents (incident_id SERIAL NOT NULL PRIMARY KEY,createdOn TEXT NOT NULL, createdBy TEXT NOT NULL, incType TEXT NOT NULL, location TEXT NOT NULL, status TEXT NOT NULL, image TEXT NOT NULL, video TEXT NOT NULL, comment TEXT NOT NULL);"
            self.cursor.execute(create_incident_table)
        except:
            pprint('Failed to connect to the database')

    def user_signup(self, firstname, lastname, othernames, email, phone_number, username, password, registered, isadmin):
        query = f"INSERT INTO users(firstname, lastname, othernames, email, phone_number, username, password, registered, isadmin) VALUES('{firstname}', '{lastname}', '{othernames}', '{email}', '{phone_number}','{username}', '{password}','{registered}', 'False');"
        pprint(query)
        self.cursor.execute(query)

    def check_username(self, username):
        query = f"SELECT * FROM users WHERE username='{username}';"
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def check_email(self, email):
        query = f"SELECT * FROM users WHERE email='{email}';"
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def login(self, username):
        query = f"SELECT * FROM users WHERE username='{username}';"
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        pprint(user)
        return user

    def query_one(self, incident_id):
        query = f"SELECT * FROM incidents WHERE incident_id = '{incident_id}';"
        pprint(query)
        self.cursor.execute(query)
        incident= self.cursor.fetchall()
        pprint(incident)
        return incident

    def query_all(self, table):
        query = f"SELECT * FROM {table};"
        pprint(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        pprint(result)
        return result

    def insert_incident(self, createdOn, createdBy, incType, location, status, image, video,comment):
        query = f"INSERT INTO incidents(createdOn, createdBy, incType, location, status, image, video,comment) VALUES ('{createdOn}', '{createdBy}', '{incType}', '{location}', '{status}', '{image}', '{video}', '{comment}');"
        pprint(query)
        self.cursor.execute(query)

    def update(self, table, column, new_value, cell, incident_id):
        query = f"UPDATE {table} SET {column}='{new_value}' WHERE {cell}='{incident_id}';"
        pprint(query)
        self.cursor.execute(query)

    def delete(self, table, cell, incident_id):
        query = f"DELETE FROM {table} WHERE {cell} = '{incident_id}';"
        pprint(query)
        self.cursor.execute(query)

    def drop_table(self, table_name):
        drop = f"DROP TABLE {table_name};"
        self.cursor.execute(drop)



# if __name__ == "__main__":
#     db = DatabaseConnection()
