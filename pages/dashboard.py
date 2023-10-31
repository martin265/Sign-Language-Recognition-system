import flet as ft
from classes.student import Student
from connection.db import my_connection
from datetime import datetime
from pages.Sign_language_detection.inference_classifier import AllSigns
from templates.header import Header


class Dashboard(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.database_cursor = my_connection.cursor()
        self.editDelete_id = ft.Text()
        self.first_name = ft.TextField(width=450, label="first name", hint_text="required field",
                                       helper_text="only characters", filled=True,
                                       prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
                                       focused_border_color="#1a237e", focused_color="#6200ea"
                                       )
        self.last_name = ft.TextField(width=450, label="last name", hint_text="required field",
                                      helper_text="only characters",
                                      filled=True,
                                      prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
                                      focused_border_color="#1a237e", focused_color="#6200ea"
                                      )
        self.age = ft.TextField(width=450, label="enter your age",
                                hint_text="required field",
                                filled=True,
                                helper_text="only characters",
                                prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
                                focused_border_color="#1a237e", focused_color="#6200ea"
                                )
        self.gender = ft.RadioGroup(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "gender",
                        size=18,
                        weight=ft.FontWeight.W_700
                    ),
                    ft.Radio(value="male", label="male"),
                    ft.Radio(value="female", label="female")
                ]
            )
        )
        self.grade = ft.Dropdown(
            label="select grade....",
            filled=True,
            hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            width=450,
            options=[
                ft.dropdown.Option("Level 4"),
                ft.dropdown.Option("Level 5"),
                ft.dropdown.Option("Level 6")
            ]
        )
        self.phone_number = ft.TextField(
            width=450,
            label="enter your phone number....",
            hint_text="required field",
            filled=True,
            helper_text="only characters",
            prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea"
        )
        self.address = ft.TextField(
            width=450,
            filled=True,
            label="enter your address...",
            hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea"
        )
        self.course = ft.Dropdown(
            label="select course....",
            hint_text="required field",
            filled=True,
            helper_text="only characters",
            prefix_icon=ft.icons.PHONE_IPHONE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            width=450,
            options=[
                ft.dropdown.Option("Mathematics"),
                ft.dropdown.Option("Social Studies"),
                ft.dropdown.Option("Biology"),
                ft.dropdown.Option("Physical science"),
                ft.dropdown.Option("Geography"),
            ]
        )
        #  ------------------the student table here-----------------------//
        self.student_table = ft.DataTable(
            width=1050,
            horizontal_margin=10,
            sort_column_index=0,
            height=400,
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
                ft.DataColumn(ft.Text("operations".capitalize())),

            ],
            rows=[]
        )
        #  -------------------------the subject table here----------------------------//
        self.subject_table = ft.DataTable(
            width=1050,
            horizontal_margin=10,
            sort_column_index=0,
            height=400,
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
                ft.DataColumn(ft.Text("operations".capitalize())),

            ],
            rows=[]
        )
        self.delete_dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete that record?"),
            actions=[
                ft.TextButton("Yes", on_click=self.delete_record),
                ft.TextButton("No", on_click=self.close_delete_modal)
            ]
        )

    #  --------------------functions to update and delete student records-----------------------//
    def close_delete_modal(self, e):
        self.page.dialog = self.delete_dlg_modal
        self.delete_dlg_modal.open = False
        self.page.update()

    def build(self):
        self.show_table_data()
        self.show_subject_table()
        return ft.ListView(
            expand=True,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=700,
            scale=1.0,
            controls=[
                Header(),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            #  ------------------the container will keep the top page---------//
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=20),
                                bgcolor="#F2ECFF",
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Card(
                                                    content=ft.Container(
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                "#00B4C6",
                                                                "#007BDD"
                                                            ],
                                                            begin=ft.alignment.bottom_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        border_radius=ft.border_radius.all(10),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    padding=ft.padding.only(left=200),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.icons.LIGHT_MODE_ROUNDED,
                                                                                size=40,
                                                                                color="#FFBB4D"
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(
                                                                    padding=ft.padding.only(left=10, right=10),
                                                                    margin=ft.margin.only(bottom=20),
                                                                    width=300,
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Text(
                                                                                "the system will translate your uploaded"
                                                                                "text inputs to braille codes and later printed."
                                                                                "the braille dots will be generated with the"
                                                                                "accuracy of 98.9% as predicted by the machine "
                                                                                "learning models".capitalize(),
                                                                                weight=ft.FontWeight.W_500,
                                                                                size=15,
                                                                                color="white"
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ),

                                                #  -------------------second hard----------------//
                                                ft.Card(
                                                    content=ft.Container(
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                "#00B4C6",
                                                                "#007BDD"
                                                            ],
                                                            begin=ft.alignment.bottom_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        border_radius=ft.border_radius.all(10),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    padding=ft.padding.only(left=200),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.icons.LIGHT_MODE_ROUNDED,
                                                                                size=40,
                                                                                color="#FFBB4D"
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(
                                                                    padding=ft.padding.only(left=10, right=10),
                                                                    margin=ft.margin.only(bottom=20),
                                                                    width=300,
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Text(
                                                                                "the system will translate your uploaded"
                                                                                "text inputs to braille codes and later printed."
                                                                                "the braille dots will be generated with the"
                                                                                "accuracy of 98.9% as predicted by the machine "
                                                                                "learning models".capitalize(),
                                                                                weight=ft.FontWeight.W_500,
                                                                                size=15,
                                                                                color="white"
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ),

                                                #  ----------------------------//------------------

                                                ft.Card(
                                                    content=ft.Container(
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                "#00B4C6",
                                                                "#007BDD"
                                                            ],
                                                            begin=ft.alignment.bottom_left,
                                                            end=ft.alignment.top_right
                                                        ),
                                                        border_radius=ft.border_radius.all(10),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    padding=ft.padding.only(left=200),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.icons.LIGHT_MODE_ROUNDED,
                                                                                size=40,
                                                                                color="#FFBB4D"
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(
                                                                    padding=ft.padding.only(left=10, right=10),
                                                                    margin=ft.margin.only(bottom=20),
                                                                    width=300,
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Text(
                                                                                "the system will translate your uploaded"
                                                                                "text inputs to braille codes and later printed."
                                                                                "the braille dots will be generated with the"
                                                                                "accuracy of 98.9% as predicted by the machine "
                                                                                "learning models".capitalize(),
                                                                                weight=ft.FontWeight.W_500,
                                                                                size=15,
                                                                                color="white"
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ),
                            #  --------------------the other container will be here----------//
                            ft.Container(),
                            #  --------------------//-----------------//----------//
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(bottom=30),
                                margin=ft.margin.only(right=20),
                                bgcolor="#F2ECFF",
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Tabs(
                                                    scrollable=True,
                                                    animation_duration=10,
                                                    animate_size=900,
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
                                                                            "students".title(),
                                                                            weight=ft.FontWeight.W_700
                                                                        )
                                                                    ]
                                                                )
                                                            ),
                                                            content=ft.Container(
                                                                margin=ft.margin.only(top=20),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
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
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.BOOK_ROUNDED,
                                                                        ),
                                                                        ft.Text(
                                                                            "subject details".title(),
                                                                            weight=ft.FontWeight.W_700
                                                                        )
                                                                    ]
                                                                )
                                                            ),
                                                            content=ft.Container(
                                                                margin=ft.margin.only(top=20),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.subject_table
                                                                    ]
                                                                )
                                                            ),
                                                        ),
                                                    ],
                                                    width=1100,
                                                    height=400
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )

    def show_table_data(self):
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
                        ft.DataCell(ft.Text(single_record["first_name"][:7])),
                        ft.DataCell(ft.Text(single_record["last_name"])),
                        ft.DataCell(ft.Text(single_record["age"])),
                        ft.DataCell(ft.Text(single_record["gender"])),
                        ft.DataCell(ft.Text(single_record["grade"][:5])),
                        ft.DataCell(ft.Text(single_record["phone_number"])),
                        ft.DataCell(ft.Text(single_record["address"][:10])),
                        ft.DataCell(ft.Text(single_record["course"])),
                        ft.DataCell(ft.Text(single_record["date_registered"])),
                        #  --------------the delete and update controls------------//
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.UPDATE_ROUNDED,
                                        on_click={},
                                        tooltip="update",
                                        icon_color="#00B4C6",
                                    ),
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.DELETE_ROUNDED,
                                        on_click=self.fill_delete_id,
                                        tooltip="delete",
                                        icon_color="#f44336"
                                    ),
                                    #  ------------------deleting and updating the records-------//
                                ]
                            )
                        ),

                    ]
                )
            )
            self.update_dlg_modal = ft.AlertDialog(
                modal=True,
                content=ft.Container(
                    width=450,
                    content=ft.Column(
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            self.first_name,
                            self.last_name,
                            self.age,
                            self.gender,
                            self.grade,
                            self.phone_number,
                            self.address,
                            self.course,
                            #  -------------the controls to update the records here----------//
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="update record",
                                            on_click=self.update_records
                                        ),
                                        ft.ElevatedButton(
                                            text="update record",
                                            on_click=self.close_update_modal
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )

    def close_update_modal(self, e):
        self.page.dialog = self.update_dlg_modal
        self.update_dlg_modal.open = False
        self.page.update()

    def fill_delete_id(self, e):
        self.editDelete_id = e.control.data["id"]
        self.page.dialog = self.delete_dlg_modal
        self.delete_dlg_modal.open = True
        self.page.update()

    def delete_record(self, e):
        """the function to delete record from the database here"""
        try:
             
            #  -----------------creating the student object here----------------//
            student = Student(self.first_name.value, self.last_name.value, self.age.value, self.gender.value,
                              self.grade.value, self.phone_number.value, self.address.value, self.course.value)
            # ----------------------------------------//-------------------------//
            student.delete_student_record(current_id)
            self.page.snack_bar = ft.SnackBar(
                bgcolor=ft.colors.RED_700,
                content=ft.Text("record deleted successfully".title()),
                action="OK"
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.delete_dlg_modal.open = False
            self.page.update()

        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title()
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()

    def update_records(self, e):
        try:
            new_first_name = self.first_name.value
            new_last_name = self.last_name.value
            new_age = self.age.value
            new_gender = self.gender.value
            new_grade = self.grade.value
            new_phone_number = self.phone_number.value
            new_address = self.address.value
            new_course = self.course.value
            new_date = datetime.now()
            id_to_update = self.editDelete_id
            # -----------------calling the object of the class here----------------//
            student = Student(new_first_name, new_last_name, new_age, new_gender, new_grade, new_phone_number,
                              new_address, new_course)
            student.update_student_record(id_to_update)
            self.update_dlg_modal.open = False
            self.page.snack_bar = ft.SnackBar(
                ft.Text("record updated successfully"),
                action="ok".title(),
                bgcolor="green"
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title()
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()

    def fill_text_boxes(self, e):
        """the function to prefill the text-boxes when the button is clicked here-------"""
        try:
            self.editDelete_id = e.control.data["id"]
            self.first_name.value = e.control.data["first_name"]
            self.last_name.value = e.control.data["last_name"]
            self.age.value = e.control.data["age"]
            self.gender.value = e.control.data["gender"]
            self.grade.value = e.control.data["grade"]
            self.phone_number.value = e.control.data["phone_number"]
            self.address.value = e.control.data["address"]
            self.course.value = e.control.data["course"]

            self.page.dialog = self.update_dlg_modal
            self.update_dlg_modal.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    bgcolor="red",
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title()
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()

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
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.UPDATE_ROUNDED,
                                        on_click={},
                                        tooltip="update",
                                        icon_color="#00B4C6",
                                    ),
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.DELETE_ROUNDED,
                                        on_click={},
                                        tooltip="delete",
                                        icon_color="#f44336"
                                    ),
                                    #  ------------------deleting and updating the records-------//
                                ]
                            )
                        ),

                    ]
                )
            )
