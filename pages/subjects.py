import datetime
import flet as ft
from connection.db import my_connection
import random
from classes.subject import Subject
from datetime import datetime


class Subjects(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.editDelete_id = ft.Text()
        self.database_cursor = my_connection.cursor()
        self.random_code = random.randint(1, 900)
        self.lecture_name = ft.Text()
        self.single_record = ""
        self.total_subjects = 0
        #   --------------getting the user inputs here--------------------//
        self.subject_name = ft.TextField(
            width=500, label="subject name".title(), hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            border_color="#009CDC",
        )
        self.gender = ft.TextField(
            width=500, label="subject code".title(), hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.QR_CODE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            value=f"{self.random_code}",
            border_color="#009CDC",
            on_change=self.random_code
        ),
        self.subject_code = ft.TextField(
            width=500, label="subject code".title(), hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.QR_CODE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            value=f"{self.random_code}",
            border_color="#009CDC",
            on_change=self.random_code
        )
        self.subject_description = ft.TextField(
            width=500, label="subject description".title(), hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.DESCRIPTION_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            multiline=True,
            min_lines=1,
            max_lines=5,
            border_color="#009CDC",
        )
        self.subject_duration = ft.Dropdown(
            label="select duration....",
            helper_text="select the preferred duration",
            width=500,
            border_color="#009CDC",
            options=[
                ft.dropdown.Option("a year"),
                ft.dropdown.Option("2 years"),
                ft.dropdown.Option("4 years"),
                ft.dropdown.Option("6 years")
            ]
        )
        self.assigned_lecture = ft.Dropdown(
            label="select lecture....",
            helper_text="select lecture",
            filled=True,
            width=500,
            dense=True,
            options=[

            ]
        )
        #  ---------filling the combox with the required values here---------------//

        #  ----------------------the filling of data ends here------------//
        self.update_modal = ft.AlertDialog(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        self.assigned_lecture
                    ]
                )
            )
        )

        self.current_subjects = ft.GridView(
            expand=1,
            runs_count=6,
            max_extent=300,
            child_aspect_ratio=0.9,
            spacing=1,
            run_spacing=5,
            padding=30,
            width=300,
        )

    #  --------------------closing the update modal here--------------//
    def close_modal_page(self, e):
        self.page.dialog = self.update_modal
        self.update_modal.open = False
        self.page.update()

    def trigger_drop_down(self):
        sql = "SELECT first_name FROM Lecture"
        self.database_cursor.execute(sql)
        all_results = self.database_cursor.fetchall()
        #  ----------pushing the data to the main table here----------------//
        columns = [column[0] for column in self.database_cursor.description]
        rows = [dict(zip(columns, row)) for row in all_results]

        #  ----------------looping through all the records here-------------//
        for lecture_name in rows:
            for keys in lecture_name.values():
                self.assigned_lecture.options.append(
                    ft.dropdown.Option(
                        keys
                    )
                )

    def validate_input_fields(self, e):
        try:
            if not self.subject_name.value:
                self.subject_name.error_text = "please fill in the blanks".title()
                self.update()
            #  -------------------validating the subject code here-----------//
            elif not self.subject_code.value:
                self.subject_code.error_text = "please fill in the blanks".title()
                self.update()
            #  -------------------validating the subject code here-----------//
            elif not self.subject_description.value:
                self.subject_description.error_text = "please fill in the blanks".title()
                self.update()
            #  -------------------validating the subject code here-----------//
            elif not self.subject_duration.value:
                self.subject_duration.error_text = "please fill in the blanks".title()
                self.update()
            #  -------------------validating the subject code here-----------//
            elif not self.assigned_lecture.value:
                self.assigned_lecture.error_text = "please fill in the blanks".title()
                self.update()
            else:
                self.save_record()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection".title()
                    )
                )
            )

    def AllSubjects(self):
        try:
            sql = "SELECT COUNT(*) FROM Lecture"
            self.database_cursor.execute(sql)
            all_results = self.database_cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in self.database_cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]
            self.total_subjects = rows
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

    def build(self):
        self.trigger_drop_down()
        self.AllSubjects()
        self.display_registered_record()
        return ft.ListView(
            expand=True,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=700,
            scale=1.0,
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            #  -----------------the top container here---------------//
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                self.current_subjects
                                            ]
                                        )
                                    ]
                                )
                            ),
                            #  ----------------------the second container----------------//
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=20),
                                bgcolor="#F2ECFF",
                                content=ft.Column(
                                    controls=[
                                        ft.Row([self.subject_name, self.subject_code]),
                                        ft.Row([self.subject_description, self.subject_duration]),
                                        ft.Row([self.assigned_lecture, ]),

                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        on_click=self.validate_input_fields,
                                                        bgcolor="#007BDD",
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.SAVE_ROUNDED,
                                                                    size=20,
                                                                    color="white"),
                                                                ft.Text(
                                                                    "save subject details".title(),
                                                                    color="white"
                                                                )
                                                            ],
                                                        ),
                                                    ),
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]
        )

    #  -----------------------saving the details to the database here-------------------//
    def save_record(self):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            subject = Subject(
                self.subject_name.value,
                self.subject_code.value,
                self.subject_description.value,
                self.subject_duration.value,
                self.assigned_lecture.value,
                current_date
            )
            subject.add_new_subject()
            self.clear_text_boxes()
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#007BDD",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "lecture records save successfully".capitalize(),
                                size=24,
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    def clear_text_boxes(self):
        try:
            self.subject_name.value = ""
            self.subject_code.value = ""
            self.subject_description.value = ""
            self.subject_duration.value = ""
            self.assigned_lecture.value = ""
            self.update()
        except Exception as ex:
            print(ex)

    #  -------------------fetching all data in the database here--------------//
    def display_registered_record(self):
        try:
            sql = "SELECT * FROM subject LIMIT 4"
            database_cursor = my_connection.cursor()
            database_cursor.execute(sql)
            all_results = database_cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in database_cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]

            for self.single_record in rows:
                self.current_subjects.controls.append(
                    ft.Card(
                        elevation=0.5,
                        content=ft.Container(
                            bgcolor="#F2ECFF",
                            border_radius=ft.border_radius.all(10),
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.only(left=20, top=20, right=20),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.API_ROUNDED,
                                                    icon_size=30,
                                                    icon_color="black",
                                                    tooltip="show more",
                                                    bgcolor="white"
                                                )
                                            ]
                                        )
                                    ),
                                    #  ----------------the container for the circle avatar---------//
                                    ft.Container(
                                        margin=ft.margin.only(top=30),
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.CircleAvatar(
                                                    bgcolor="#007BDD",
                                                    width=150,
                                                    height=150,
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                f"{self.single_record['subject_name']}".capitalize(),
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    )
                )
        except Exception as ex:
            print(ex)
