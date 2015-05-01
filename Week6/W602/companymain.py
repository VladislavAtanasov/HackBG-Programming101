import sqlite3
from manage_company import Connect
from database import DataWork

def main():
    new_data = DataWork()
    command = "Enter help to see the commands: "
    print(command)
    while command != "exit":
        command = input("command> ")
        if command == "list_employees":
            print(new_data.list_employees())
        elif command == "monthly_spending":
            print("The company is spending ${} every month!".format(new_data.monthly_spending()))
        elif command == "yearly_spending":
            print(new_data.yearly_spending())
        elif "delete_employee " in command:
            string = str(command)
            dig = string[string.index(" "):]
            digit = int(dig)
            print(new_data.delete_employee(digit))
        elif command == "add_employee":
            print(new_data.add_employee())
        elif "update_employee " in command:
            string = str(command)
            dig = string[string.index(" "):]
            digit = int(dig)
            print(new_data.update_employee(digit))
        elif command == "help":
            print("""List of commands:
                list_employees
                monthly_spending
                yearly_spending
                add_employee
                delete_employee <id>
                update_employee <id>
                exit
                """)
        elif command != "exit":
            raise Exception("No such command")
    print("You exited the App!")

if __name__ == '__main__':
    main()
