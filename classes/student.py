import flet as ft
from connection.db import my_connection


class Student:

    def __init__(self, first_name, last_name, age, gender, grade, phone_number, address, course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.grade = grade
        self.phone_number = phone_number
        self.address = address
        self.course = course
        self.database_cursor = my_connection.cursor()

    #  --------------method to add new student to the details-----------------//
    def add_new_student_details(self):
        """the method to add a new student to the system"""
        try:
            sql = "INSERT INTO Students(first_name, last_name, age, gender, grade, phone_number, address, course) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.first_name, self.last_name, self.age, self.gender, self.grade, self.phone_number, self.address,
                   self.course)
            self.database_cursor.execute(sql, val)
            my_connection.commit()

        except Exception as ex:
            print(ex)

    #  ---------------method to update the student records------------------//
    def update_student_record(self, current_student_id):
        """the method to update the student records here for the system"""
        try:
            sql = "UPDATE Students SET first_name = %s, last_name = %s, age = %s, gender=%s, grade = %s, phone_number = %s, address = %s, course = %s WHERE id = %s"
            values = (
                self.first_name, self.last_name, self.age, self.gender, self.grade, self.phone_number, self.address,
                self.course, current_student_id)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  ---------------method to update the student records------------------//
    def delete_student_record(self, current_student_id):
        """the method to delete the student records here for the system"""
        try:
            sql = "DELETE FROM Students WHERE id = %s"
            values = (current_student_id,)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)