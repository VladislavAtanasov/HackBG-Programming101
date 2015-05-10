import sqlite3
import requests
from lastHR import HR

class Database:

    def __init__(self, filename):
        self.hr = HR()
        self.db = sqlite3.connect(filename)
        self.cursor = self.db.cursor()
        self.information = self.hr.read("data4.json")

    def create_students(self):
        create_table = """
        CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, github TEXT)
        """
        self.cursor.execute(create_table)
        self.db.commit()
        return "A table students was created"

    def insert_in_students_query(self, human, gh):
        return self.cursor.execute("INSERT INTO students(name, github) VALUES(?, ?)", (human, gh))

    def insert_in_students(self):
        for item in self.information:
            self.insert_in_students_query(item["name"], item["github"])
        return self.db.commit()

    def create_courses(self):
        create_table = """
        CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY, course TEXT)
        """
        self.cursor.execute(create_table)
        return self.db.commit()

    def insert_in_courses_query(self, course_name):
        return self.cursor.execute("INSERT INTO courses(course) VALUES (?)", (course_name, ))

    def insert_in_courses(self):
        courses_list = set()
        for item in self.information:
            for x in item["courses"]:
                courses_list.add(x['name'])
        for item in courses_list:
            self.insert_in_courses_query(item)
        return self.db.commit()

    def create_students_courses(self):
        create_stud_courses = """CREATE TABLE IF NOT EXISTS stud_courses(
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id))"""
        self.cursor.execute(create_stud_courses)
        return self.db.commit()

    def get_course_id(self, course_name):
        course = self.cursor.execute("""SELECT id FROM courses
                                WHERE course = ?""", (course_name,))
        return course.fetchone()[0]

    def get_name_id(self, name):
        username = self.cursor.execute("""SELECT id FROM students
                                WHERE name = ?""", (name,))
        return username.fetchone()[0]

    def insert_names_courses_query(self, user_name, course_name):
        return self.cursor.execute("INSERT INTO stud_courses(student_id, course_id) VALUES (?, ?)", (user_name, course_name))

    def insert_stud_courses(self):
        for user in self.information:
            for course in user["courses"]:
                    self.insert_names_courses_query(self.get_name_id(user["name"]), self.get_course_id(course['name']))
        return self.db.commit()

    def get_student_with_most_courses(self):
        students = self.cursor.execute("""SELECT name
                FROM students S
                INNER JOIN stud_courses AS StoC
                ON S.id = StoC.student_id
                GROUP BY StoC.student_id
                ORDER BY COUNT(StoC.student_id) DESC
                LIMIT 5""")
        for stud in students:
            print(stud[0])


def main():
    data = Database("hr_database.db")
    data.create_students()
    data.create_courses()
    data.create_students_courses()
    data.get_student_with_most_courses()

if __name__ == '__main__':
    main()
