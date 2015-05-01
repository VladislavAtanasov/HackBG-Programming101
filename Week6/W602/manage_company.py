import sqlite3

class Connect:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def list_employees(self):
        return self.cursor.execute("SELECT id, name, position FROM company")

    def monthly_spending(self):
        return self.cursor.execute("SELECT monthly_salary FROM company")

    def yearly_spending(self):
        return self.cursor.execute("SELECT yearly_bonus FROM company")

    def delete_employee(self, number):
        return self.cursor.execute("DELETE FROM company WHERE id = %d" %(number))

    def add_employee(self, value):
        return self.cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES (?,?,?,?)", (value[0],value[1],value[2],value[3]))

    def update_employee(self, value, number):
        return self.cursor.execute("UPDATE company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ?", (value[0],value[1],value[2],value[3], number))

    def name_by_id(self, num):
        names = self.cursor.execute("SELECT name FROM company WHERE id = %d" %(num))
        for x in names:
            return x[0]

    def user_commands(self):
        user_input = tuple()
        for command in ["name>","monthly_salary>","yearly_bonus>","position>"]:
            response = input(command)
            user_input += (response,)
        return user_input

    def list_id(self):
        list_id = []
        ids = self.cursor.execute("SELECT id FROM company")
        for elem in ids:
            list_id.append(elem[0])
        return list_id

def main():
    pass
    #comp = Connect("create_company.db")
    #command = input("command> ")
    #while command != "exit":
    #    if command == "list_employees":
    #        pass
    #    elif command == "monthly_spending":
    #        pass
    #    elif command == "yearly_spending":
    #        pass
    #    elif command == "add_employee":
    #        pass
    #    elif command == "delete_employee <employee_id>":
    #        pass
    #    elif command == "update_employee <employee_id>":
    #        pass

if __name__ == '__main__':
    main()
