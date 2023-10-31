import flet as ft
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from connection.db import my_connection
import subprocess
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from docx.shared import Inches
from reportlab.pdfgen import canvas


class Reports(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()
        self.recording_name = ft.Text()
        self.student_table = ft.DataTable(
            width=1050,
            horizontal_margin=10,
            sort_column_index=0,
            height=700,
            sort_ascending=True,
            column_spacing=5,
            bgcolor="white",
            heading_text_style=ft.TextStyle(
                size=15,
                weight=ft.FontWeight.BOLD,
                color="#007BDD",
            ),
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(1, "#f5f5f5"),
            columns=[
                ft.DataColumn(ft.Text("first name".capitalize())),
                ft.DataColumn(ft.Text("last name".capitalize())),
                ft.DataColumn(ft.Text("age".capitalize())),
                ft.DataColumn(ft.Text("gender".capitalize())),
                ft.DataColumn(ft.Text("grade".capitalize())),
                ft.DataColumn(ft.Text("phone number".capitalize())),
                ft.DataColumn(ft.Text("address".capitalize())),
                ft.DataColumn(ft.Text("course".capitalize())),
                ft.DataColumn(ft.Text("date registered".capitalize())),
            ],
            rows=[]
        )
        self.subject_table = ft.DataTable(
            width=1050,
            horizontal_margin=10,
            sort_column_index=0,
            height=600,
            sort_ascending=True,
            column_spacing=5,
            bgcolor="white",
            heading_text_style=ft.TextStyle(
                size=15,
                weight=ft.FontWeight.BOLD,
                color="#007BDD",
            ),
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(1, "#f5f5f5"),
            columns=[
                ft.DataColumn(ft.Text("subject name".capitalize())),
                ft.DataColumn(ft.Text("subject code".capitalize())),
                ft.DataColumn(ft.Text("subject description".capitalize())),
                ft.DataColumn(ft.Text("subject duration".capitalize())),
                ft.DataColumn(ft.Text("assigned lecture".capitalize())),
                ft.DataColumn(ft.Text("added date".capitalize())),
            ],
            rows=[]
        )
        self.document_name = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="enter the document_name",
            hint_text="document name",
            autofocus=True,
            helper_text="select time(S)...",
            prefix_icon=ft.icons.DOCUMENT_SCANNER_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
        )

    def build(self):
        self.show_student_data()
        self.show_subject_table()
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=700,
            controls=[
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                    margin=ft.margin.only(right=20, top=30),
                    bgcolor="#f5f5f5",
                    height=700,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.ElevatedButton(

                                            on_click=self.export_to_word,
                                            bgcolor="#007BDD",
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.BROADCAST_ON_HOME_ROUNDED,
                                                        size=20,
                                                        color="white"),
                                                    ft.Text(
                                                        "print out report".title(),
                                                        color="white"
                                                    )
                                                ],
                                            ),
                                        ),
                                    ]
                                )
                            ),

                            ft.Tabs(
                                scrollable=True,
                                animation_duration=9,
                                animate_size=300,
                                selected_index=0,
                                tabs=[
                                    ft.Tab(
                                        tab_content=ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.PEOPLE_ROUNDED,
                                                    ),
                                                    ft.Text(
                                                        "Student Records".title(),
                                                        weight=ft.FontWeight.W_700
                                                    )
                                                ]
                                            )
                                        ),
                                        content=ft.Container(
                                            margin=ft.margin.only(top=10),
                                            content=ft.Row(
                                                controls=[
                                                    self.student_table
                                                ]
                                            )
                                        ),
                                    ),
                                    #  -----------------//-----------------
                                    ft.Tab(
                                        tab_content=ft.Container(
                                            content=ft.Row(
                                                scroll=ft.ScrollMode.ALWAYS,
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.LIBRARY_BOOKS_ROUNDED,
                                                    ),
                                                    ft.Text(
                                                        "Subject Records".title(),
                                                        weight=ft.FontWeight.W_700
                                                    )
                                                ]
                                            )
                                        ),
                                        content=ft.Container(
                                            margin=ft.margin.only(top=10),
                                            content=ft.Row(
                                                controls=[
                                                    self.subject_table
                                                ]
                                            )
                                        ),
                                    ),
                                ],
                                width=1100,
                                height=600
                            )
                        ]
                    )
                )
            ]
        )

    def show_student_data(self):
        sql = "SELECT * FROM Students"
        self.database_cursor.execute(sql)
        all_results = self.database_cursor.fetchall()
        #  ----------pushing the data to the main table here----------------//
        columns = [column[0] for column in self.database_cursor.description]
        rows = [dict(zip(columns, row)) for row in all_results]

        for single_record in rows:
            self.student_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(single_record["first_name"])),
                        ft.DataCell(ft.Text(single_record["last_name"])),
                        ft.DataCell(ft.Text(single_record["age"])),
                        ft.DataCell(ft.Text(single_record["gender"])),
                        ft.DataCell(ft.Text(single_record["grade"][:5])),
                        ft.DataCell(ft.Text(single_record["phone_number"])),
                        ft.DataCell(ft.Text(single_record["address"][:10])),
                        ft.DataCell(ft.Text(single_record["course"])),
                        ft.DataCell(ft.Text(single_record["date_registered"])),
                    ]
                )
            )

    def export_to_word(self, e):
        try:
            sql = "SELECT * FROM Students"
            cursor = my_connection.cursor()
            cursor.execute(sql)
            all_results = cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]
            for results in rows:
                all_table_data = ft.AlertDialog(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text("")
                                ]
                            )
                        ]
                    )
                )
                self.page.dialog = all_table_data
                self.page.update()

            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "your document has been saved successfully".capitalize(),
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                weight=ft.FontWeight.W_700,
                                color="white"
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    #  -------------------getting all the subjects here--------------------------//
    def show_subject_table(self):
        sql = "SELECT * FROM Subject"
        self.database_cursor.execute(sql)
        all_results = self.database_cursor.fetchall()
        #  ----------pushing the data to the main table here----------------//
        columns = [column[0] for column in self.database_cursor.description]
        rows = [dict(zip(columns, row)) for row in all_results]

        for single_record in rows:
            self.subject_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(single_record["subject_name"])),
                        ft.DataCell(ft.Text(single_record["subject_code"])),
                        ft.DataCell(ft.Text(single_record["subject_description"][:10])),
                        ft.DataCell(ft.Text(single_record["subject_duration"])),
                        ft.DataCell(ft.Text(single_record["assigned_lecture"])),
                        ft.DataCell(ft.Text(single_record["added_date"])),
                        #  --------------the delete and update controls------------//
                    ]
                )
            )
