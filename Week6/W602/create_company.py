import sqlite3
def main():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS company(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
    """

    db = sqlite3.connect("companydb.db")
    cursor = db.cursor()
    cursor.execute(create_table_query)
    insert_row = """
    INSERT INTO company(name, monthly_salary, yearly_bonus, position)
    VALUES ("Ivan Ivanov", 5000, 10000, "Software Developer"),
           ("Rado Rado", 500, 0, "Technical Support Intern"),
           ("Ivo Ivo", 10000, 100000, "CEO"),
           ("Petar Petrov", 3000, 1000, "Marketing Manager"),
           ("Maria Georgieva", 8000, 10000, "COO")
    """
    cursor.execute(insert_row)
    db.commit()
    #cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)", (name1, monthly_salary1, yearly_bonus1, position1))
    #cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)", (name2, monthly_salary2, yearly_bonus2, position2))
    #cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)", (name3, monthly_salary3, yearly_bonus3, position3))
    #cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)", (name4, monthly_salary4, yearly_bonus4, position4))
    #cursor.execute("INSERT INTO company(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)", (name5, monthly_salary5, yearly_bonus5, position5))
    #name1 = "Ivan Ivanov"
    #monthly_salary1 = 5000
    #yearly_bonus1 = 10000
    #position1 = "Software Developer"
#
#    #name2 = "Rado Rado"
#    #monthly_salary2 = 500
#    #yearly_bonus2 = 0
#    #position2 = "Technical Support Intern"
#
#    #name3 = "Ivo Ivo"
#    #monthly_salary3 = 10000
#    #yearly_bonus3 = 100000
#    #position3 = "CEO"
#
#    #name4 = "Petar Petrov"
#    #monthly_salary4 = 3000
#    #yearly_bonus4 = 1000
#    #position4 = "Marketing Manager"
#
#    #name5 = "Maria Georgieva"
#    #monthly_salary5 = 8000
#    #yearly_bonus5 = 10000
    #position5 = "COO"



if __name__ == '__main__':
    main()
