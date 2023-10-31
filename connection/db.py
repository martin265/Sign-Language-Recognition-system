import os
import flet as ft
import mysql.connector
from flet import Page

#  ---------the function to create the new table here-------------//
try:
    my_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="language"
    )
    if my_connection:
        print("")
    else:
        print("failed to connect with the database")
except Exception as ex:
    print(ex)


#  ---------------------the student table---------------------//
def create_student_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE Students(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "first_name VARCHAR(50) NOT NULL," \
              "last_name VARCHAR(50) NOT NULL," \
              "age VARCHAR(50) NOT NULL," \
              "gender VARCHAR(50) NOT NULL," \
              "grade VARCHAR(50) NOT NULL," \
              "phone_number VARCHAR(5) NOT NULL," \
              "address VARCHAR(50) NOT NULL," \
              "course VARCHAR(50) NOT NULL," \
              "date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
        database_cursor.execute(sql)
        my_connection.commit()
        print("student table created successfully")
    except Exception as ex:
        print(ex)


#  -----------------the lecture table here---------------//
def create_lecture_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Lecture(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "first_name VARCHAR(50) NOT NULL," \
              "last_name VARCHAR(50) NOT NULL," \
              "age VARCHAR(50) NOT NULL," \
              "gender VARCHAR(50) NOT NULL," \
              "email VARCHAR(50) NOT NULL," \
              "department VARCHAR(50) NOT NULL," \
              "phone_number VARCHAR(50) NOT NULL," \
              "teaching_experience VARCHAR(50) NOT NULL," \
              "date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"
        database_cursor.execute(sql)
        my_connection.commit()
        print("lecture table created successfully")
    except Exception as ex:
        print(ex)


#  -----------------------the subject table--------------------------------//
def create_subject_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Subject(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "subject_name VARCHAR(50) NOT NULL," \
              "subject_code VARCHAR(50) NOT NULL," \
              "subject_description VARCHAR(100) NOT NULL," \
              "subject_duration VARCHAR(50) NOT NULL," \
              "assigned_lecture VARCHAR(50) NOT NULL," \
              "added_date VARCHAR(50) NOT NULL)"
        database_cursor.execute(sql)
        my_connection.commit()
        print("subject table created successfully")
    except Exception as ex:
        print(ex)


#  ------------------------creating the table for the administrator here------------------//
def create_administrator_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Administrator(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "first_name VARCHAR(50) NOT NULL," \
              "last_name VARCHAR(50) NOT NULL," \
              "username VARCHAR(50) NOT NULL," \
              "password VARCHAR(50) NOT NULL" \
              ")"
        database_cursor.execute(sql)
        my_connection.commit()
        print("administrator table created successfully")
    except Exception as ex:
        print(ex)


#  ------------------------------the course table---------------------//
def create_course_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Course(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "course_name VARCHAR(50) NOT NULL," \
              "course_type VARCHAR(50) NOT NULL," \
              "course_lecture VARCHAR(50) NOT NULL," \
              "course_duration VARCHAR(50) NOT NULL," \
              "course_code INTEGER(20) NOT NULL," \
              "course_added_date VARCHAR(50) NOT NULL)"
        database_cursor.execute(sql)
        my_connection.commit()
        print("course table created successfully")
    except Exception as ex:
        print(ex)


def create_audio_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS Audio(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "audio_file VARCHAR(100) NOT NULL," \
              "added_date VARCHAR(50) NOT NULL)"
        database_cursor.execute(sql)
        my_connection.commit()
        print("audio table created successfully")
    except Exception as ex:
        print(ex)


def create_translations_table():
    try:
        database_cursor = my_connection.cursor()
        SQL = 'CREATE TABLE IF NOT EXISTS Translations(' \
              'id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,' \
              'word VARCHAR(100) NOT NULL,' \
              'added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)'
        database_cursor.execute(SQL)
        my_connection.commit()
        print("translations table created successfully")
    except Exception as ex:
        print(ex)

# -----------------inserting the data into table here----------------//
    def add_new_student_details(self):
        """the method to add a new student to the system"""
        try:
            sql = "INSERT INTO Students(first_name, last_name, age, gender, grade, phone_number, address, course) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                'Orran', 'Jentle', 'ojentle0@github.com', 'Male', '574-293-6401', '05 Lunder Avenue', 'Afrikaans',

            )
            cursor = my_connection.cursor()
            cursor.execute(sql, values)
            my_connection.commit()

        except Exception as ex:
            print(ex)