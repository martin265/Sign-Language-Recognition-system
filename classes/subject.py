import flet as ft
from datetime import datetime, timezone
from datetime import time
from connection.db import my_connection


class Subject:
    def __init__(self, subject_name, subject_code, subject_description, subject_duration, assigned_lecture,
                 current_date):
        self.subject_name = subject_name
        self.subject_code = subject_code
        self.subject_description = subject_description
        self.subject_duration = subject_duration
        self.assigned_lecture = assigned_lecture
        self.current_date = current_date
        self.database_cursor = my_connection.cursor()

    #  --------------------the function will be used to add a new subject to the database----------//
    def add_new_subject(self):
        """the method will save the subject details to the database"""
        try:
            sql = "INSERT INTO Subject(subject_name, subject_code, subject_description, subject_duration, assigned_lecture, added_date) VALUES(%s, %s, %s, %s, %s, %s)"
            values = (self.subject_name, self.subject_code, self.subject_description, self.subject_duration,
                      self.assigned_lecture, self.current_date)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  ----------------------the function will update the database records-----------------//
    def update_subject_records(self, current_subject_id):
        """the method will delete the record"""
        try:
            sql = "UPDATE Subject SET subject_name = %s, subject_code = %s, subject_description = %s, subject_duration = %s, assigned_lecture = %s, added_date = %s WHERE id = %s"
            values = (self.subject_name, self.subject_code, self.subject_description, self.subject_duration,
                      self.assigned_lecture, self.current_date, current_subject_id)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  -----------------------the method or function will be used to delete the record in the database--------//
    def delete_subject_record(self, current_student_id):
        """the function will be used to delete the current clicked subject"""
        try:
            sql = "DELETE FROM Subject WHERE id = %s"
            values = (current_student_id,)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)
