import sys
import unittest
import os

sys.path.append("..")

from sql_manager import Db
from test_settings import DB_NAME, SQL_TEST

class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        self.manager = Db(DB_NAME)
        self.manager.create_clients_table(SQL_TEST)
        self.manager.register('Tester', '123')

    def tearDown(self):
        self.manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("/media/vladislav/D82809082808E6FA/PythonHB/Week9/1-Money-In-The-Bank/tests/bank.db")

    def test_register(self):
        self.manager.register('Dinko', '123123')

        self.manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', '123123'))
        users_count = self.manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = self.manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = self.manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_login_sql_injection(self):
        logged_user = self.manager.login("'OR 1 = 1 --", '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.manager.login('Tester', '123')
        new_message = "podaivinototam"
        self.manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.manager.login('Tester', '123')
        new_password = "12345"
        self.manager.change_pass(new_password, logged_user)

        logged_user_new_password = self.manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
