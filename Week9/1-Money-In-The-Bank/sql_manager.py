import sqlite3
from Client import Client
import os


class Db:

    def __init__(self, dataname):
        self.conn = sqlite3.connect(dataname)
        self.cursor = self.conn.cursor()

    def create_clients_table(self, sql):
        with open(sql, "r") as f:
            self.cursor.executescript(f.read())
            self.conn.commit()

    def change_balance(self, new_balance, logged_user):
            update_sql = "UPDATE clients SET balance = ? WHERE id = ?"
            self.cursor.execute(update_sql, (new_balance, logged_user.get_id()))
            self.conn.commit()
            logged_user.set_balance(new_balance)

    def change_email(self, new_email, logged_user):
            update_sql = "UPDATE clients SET email = ? WHERE id = ?"
            self.cursor.execute(update_sql, (new_email, logged_user.get_id()))
            self.conn.commit()
            logged_user.set_email(new_email)


    def change_message(self, new_message, logged_user):
        update_sql = "UPDATE clients SET message = ? WHERE id = ?"
        self.cursor.execute(update_sql, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)


    def change_pass(self, new_pass, logged_user):
        update_sql = "UPDATE clients SET password = ? WHERE id = ?"
        self.cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        self.conn.commit()


    def register(self,username, password):
        insert_sql = "insert into clients (username, password) values (?, ?)"
        self.cursor.execute(insert_sql, (username, password))
        self.conn.commit()


    def login(self, username, password):
        select_query = "SELECT id, username, balance, message, email, password FROM clients WHERE username = ? AND password = ? LIMIT 1"
        self.cursor.execute(select_query, (username, password))
        user = self.cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3], user[4], user[5])
        else:
            return False

