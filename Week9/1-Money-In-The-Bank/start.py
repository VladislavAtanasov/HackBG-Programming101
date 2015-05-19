from sql_manager import Db
from settings import DB_NAME, SQL_FILE
import re
import hashlib
import getpass
import time
import smtplib
import random


class View:

    def __init__(self):
        self.sql_manager = Db(DB_NAME)

    def is_password_valid(self, passw, name):
        hasspec = '^(?=.*(_|[^\w])).+$'
        hascap = '^(?=.*[A-Z]).+$'
        hasdig = '^(?=.*\d).+$'
        if len(passw) <= 8:
            print("Your password is too short")
            return False
        elif name not in passw and re.match(hasdig, passw) and re.match(hascap, passw) and re.match(hasspec, passw):
            return True
        else:
            print("Your pass should contain at least one  special character, one digit and one capital character.")
            return False

    def send_email(self, email, hashed):
        gmail_user = email
        gmail_pwd = XXXXXXXXXXXX
        FROM = email
        TO = ['straightedgesociety@abv.bg']
        SUBJECT = "Testing sending using gmail"
        TEXT = hashed
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            #server.quit()
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")

    def rand_tans(self):
        tans = [random.getrandbits(128) for i in range(1, 11)]
        return tans

    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")
        wrong_tries = 1
        attacker = " "
        while True:
            command = input("$$$>")

            if command == 'register':
                username = input("Enter your username: ")
                valid = False
                while valid != True:
                    password = getpass.getpass(prompt="Enter your password: ", stream=None)
                    if self.is_password_valid(password, username):
                        hash_object = hashlib.sha1(password.encode('utf-8'))
                        hex_dig = hash_object.hexdigest()
                        self.sql_manager.register(username, hex_dig)
                        valid = True
                print("Registration Successfull")

            elif command == 'login':
                username = input("Enter your username: ")
                if username == attacker and wrong_tries > 5:
                    continue
                    time.sleep(300)
                password = getpass.getpass(prompt="Enter your password: ", stream=None)
                hash_object = hashlib.sha1(password.encode('utf-8'))
                hex_dig = hash_object.hexdigest()
                logged_user = self.sql_manager.login(username, hex_dig)

                if logged_user:
                    self.logged_menu(logged_user)
                else:
                    wrong_tries += 1
                    if wrong_tries > 1 :
                        attacker = username
                    print("Login failed")

            elif command == 'help':
                print("login - for logging in!")
                print("register - for creating new account!")
                print("exit - for closing program!")

            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def logged_menu(self, logged_user):
        count = 10
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'change-email':
                new_email = input("Enter your new email: ")
                self.sql_manager.change_email(new_email, logged_user)

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                self.sql_manager.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                self.sql_manager.change_message(new_message, logged_user)

            elif "send reset-password" in command:
                email = logged_user.get_email()
                random_hash = random.choice(["AKASJKDMASMMDNAKND", "dssdkaskkdjakdjnd", "wwkjkqdqdnqwndqw", "jdskjakakndnasa"])
                hash_object = hashlib.sha1(random_hash.encode('utf-8'))
                hex_email = hash_object.hexdigest()
                self.send_email(email, hex_email)

            elif command == "reset-password":
                hash_input = input("What hash was sent to you: ")
                if hash_input == hex_email:
                    new_pass = input("Enter your new password: ")
                    self.sql_manager.change_pass(new_pass, logged_user)
                else:
                    print("Invalid Hash")

            elif command == "deposit":
                suma = input("Enter sum to deposit: ")
                suma = int(suma)
                code = input("Enter TAN Code: ")
                if code in self.rand_tans():
                    new_account = suma + logged_user.get_balance()
                    self.sql_manager.change_balance(new_account, logged_user)
                    self.rand_tans().remove(code)
                    print("{} added".format(suma))

            elif command == "withdraw":
                try:
                    suma = int(input("Enter sum to withdraw: "))
                    if suma <= logged_user.get_balance():
                        code = input("Enter TAN Code: ")
                        if code in self.rand_tans():
                            new_account = logged_user.get_balance() - suma
                            self.sql_manager.change_balance(new_account, logged_user)
                            print("{} withdrawned").format("suma")
                            self.rand_tans().remove(code)
                    else:
                        print("Not enough Money")
                except:
                    print("Invalid sum!")

            elif command == "get-tan":
                pw = input("Enter pw again")
                hash_pass = hashlib.sha1(pw.encode('utf-8'))
                hex_pw = hash_pass.hexdigest()
                print("You have {} left".format(count))
                if hex_pw == logged_user.get_passw() and count > 0:
                    ready_tans = self.rand_tans()
                    email = logged_user.get_email()
                    self.send_email(email, ready_tans)
                    count -=1
                if count == 0:
                    ready_tans = self.rand_tans()

            elif command == "display":
                print(logged_user.get_balance())

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'exit':
                break

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing password")
                print("change-message - for changing users message")
                print("show-message - for showing users message")
                print("change-email")
                print("send reset-password")
                print("reset-password")
                print("deposit")
                print("withdraw")
                print("display")

def main():
    menu = View()
    menu.main_menu()
    #menu.sql_manager.create_clients_table("create.sql")

if __name__ == '__main__':
    main()
