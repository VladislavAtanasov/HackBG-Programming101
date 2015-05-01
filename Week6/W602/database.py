from manage_company import Connect
import sqlite3

class DataWork:

    def __init__(self):
        self.manager = Connect("companydb.db")

    def list_employees(self):
        self.manager.connection.row_factory = sqlite3.Row
        self.manager.cursor = self.manager.connection.cursor()
        employees = self.manager.list_employees()
        string = ""
        for row in employees:
            string += '{} - {} - {}'.format(row["id"], row["name"], row["position"])
            string += '\n'
        return string
    def monthly_spending(self):
        list_salary = []
        mon_spending = self.manager.monthly_spending()
        for salary in mon_spending:
            list_salary.append(salary[0])
        return sum(list_salary)

    def yearly_spending(self):
        list_bonus = []
        year_spending = self.manager.yearly_spending()
        for bonus in year_spending:
            list_bonus.append(bonus[0])
        year_sum = self.monthly_spending() * 12 + sum(list_bonus)
        return "The company is spending $%d every year!" % (year_sum)

    def delete_employee(self, num):
        if isinstance(num, int) and num in self.manager.list_id():
            name_employee = self.manager.name_by_id(num)
            self.manager.delete_employee(num)
            self.manager.connection.commit()
            return "%s was removed" % (name_employee)
        else:
            raise Exception("Invalid Command")

    def add_employee(self):
        self.manager.add_employee(self.manager.user_commands())
        self.manager.connection.commit()
        return "Added!"

    def update_employee(self, num):
        if isinstance(num, int) and num in self.manager.list_id():
            name_employee = self.manager.name_by_id(num)
            self.manager.update_employee(self.manager.user_commands(), num)
            self.manager.connection.commit()
            return "%s was updated" % (name_employee)
        else:
            raise Exception("Invalid Command")


def main():
    new = DataWork()
    print(new.list_employees())
    new.manager.connection.close()
if __name__ == '__main__':
    main()
