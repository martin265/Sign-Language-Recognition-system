import flet as ft
from connection.db import my_connection


class Lecture:
    def __init__(self, first_name, last_name, age, gender, email, department, phone_number, teaching_experience):
        self.database_cursor = my_connection.cursor()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.department = department
        self.phone_number = phone_number
        self.teaching_experience = teaching_experience

    #  -------------using asynch here to fetch data from the database here--------------------//
    def save_lecture_details(self):
        try:
            sql = "INSERT INTO Lecture(first_name, last_name, age, gender, email, department, phone_number, teaching_experience) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                self.first_name, self.last_name, self.age, self.gender, self.email, self.department, self.phone_number,
                self.teaching_experience)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  ---------------method to update the student records------------------//
    def update_lecture_record(self, current_student_id):
        """the method to update the lecture records here for the system"""
        try:
            sql = "UPDATE Lecture SET first_name = %s, last_name = %s, age = %s, gender=%s, email = %s, department = %s, phone_number = %s, teaching_experience = %s WHERE id = %s"
            values = (
                self.first_name, self.last_name, self.age, self.gender, self.email, self.department, self.phone_number,
                self.teaching_experience, current_student_id)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  -----------------------the method or function will be used to delete the record in the database--------//
    def delete_lecture_record(self, current_student_id):
        """the function will be used to delete the current clicked user"""
        try:
            sql = "DELETE FROM Lecture WHERE id = %s"
            values = (current_student_id,)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)
