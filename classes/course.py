import os
import time
import datetime
from connection.db import my_connection


class Course:
    def __init__(self, course_name, course_code, course_lecture, course_duration, course_type, course_added_date):
        self.course_name = course_name
        self.course_type = course_type
        self.course_lecture = course_lecture
        self.course_duration = course_duration
        self.course_code = course_code
        self.course_added_date = course_added_date
        self.database_cursor = my_connection.cursor()

    #  ---------------------the function to save course records-----------------//
    def add_course_details(self):
        """the function to add course details here------"""
        try:
            sql = "INSERT INTO Course(course_name, course_code, course_lecture, course_duration, course_type, course_added_date) VALUES(%s, %s, %s, %s, %s, %s)"
            values = (self.course_name, self.course_type, self.course_lecture, self.course_duration, self.course_code,
                      self.course_added_date)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  ----------------------------the function will update the course details here-----------------//
    def update_course_details(self, current_course_id):
        """------------------the function will update the records in the database-------------"""
        try:
            sql = "UPDATE Course SET course_name = %s, course_code = %s, course_lecture = %s, course_duration = %s, course_type = %s, course_added_date = %s WHERE id = %s"
            values = (self.course_name, self.course_type, self.course_lecture, self.course_duration, self.course_code,
                      self.course_added_date, current_course_id)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  -------------------------------the method will be used to delete the records in the database-----------//
    def delete_course_details(self, current_course_id):
        # try:
            sql = "DELETE FROM Course WHERE id = %s"
            values = (current_course_id,)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        # except Exception as ex:
        #     print(ex)
