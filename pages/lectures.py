import flet as ft
from classes.lecture import Lecture
import os
from connection.db import my_connection


class Lectures(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.single_record = ""
        #  --------------------getting input from the lecture here------------------//
        self.first_name = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="lecture",
            hint_text="select name",
            autofocus=True,
            helper_text="first name".capitalize(),
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            focused_border_color="#1a237e",
            focused_color="#0050C1",
        )
        #  -----------------------//---------------------------//
        self.last_name = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="last name",
            hint_text="last name",
            autofocus=True,
            helper_text="last name".capitalize(),
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            focused_border_color="#1a237e",
            focused_color="#0050C1",
        )
        #  -----------------------//---------------------------//
        self.age = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="age",
            hint_text="age",
            autofocus=True,
            helper_text="age".capitalize(),
            prefix_icon=ft.icons.NUMBERS_ROUNDED,
            focused_border_color="#1a237e",
            focused_color="#0050C1",
        )
        #  -----------------------//---------------------------//
        self.gender = ft.RadioGroup(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "gender".capitalize(),
                        size=18,
                        weight=ft.FontWeight.W_700
                    ),
                    ft.Radio(value="male", label="male".capitalize()),
                    ft.Radio(value="female", label="female".capitalize())
                ]
            )
        )
        #  -----------------------//---------------------------//
        self.email = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="email",
            hint_text="email",
            autofocus=True,
            helper_text="email".capitalize(),
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            focused_border_color="#1a237e",
            focused_color="#0050C1",
        )
        #  -----------------------//---------------------------//
        self.department = ft.Dropdown(
            label="select department....",
            width=500,
            hint_text="select department",
            helper_text="only characters",
            border_color="#0050C1",
            prefix_icon=ft.icons.GRADE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("Physics department".capitalize()),
                ft.dropdown.Option("Humanity Department".capitalize()),
                ft.dropdown.Option("Social Support Department".capitalize())
            ]
        )
        #  ----------------------------//----------------------------------//-----------//
        self.phone_number = ft.TextField(
            width=500,
            label="enter your phone number....",
            hint_text="required field",
            border_color="#0050C1",
            helper_text="only characters",
            prefix_icon=ft.icons.PHONE_ENABLED_ROUNDED,
            focused_border_color="#0050C1", focused_color="#6200ea"
        )
        self.teaching_experience = ft.Dropdown(
            label="select experience...",
            width=500,
            hint_text="select experience",
            helper_text="only characters",
            border_color="#0050C1",
            prefix_icon=ft.icons.GRADE_ROUNDED,
            focused_border_color="#0050C1", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("2 years".capitalize()),
                ft.dropdown.Option("3 years".capitalize()),
                ft.dropdown.Option("5 years".capitalize())
            ]
        )
        #  ----------------------------//----------------------------------//-----------//

        #  ---------------------grid container for the profiles here-------------------//
        self.registered_lectures = ft.GridView(
            expand=1,
            runs_count=6,
            max_extent=300,
            child_aspect_ratio=0.9,
            spacing=1,
            run_spacing=5,
            padding=30,
            width=300,
        )

    #  -----------------validating the user input here--------------------//
    def input_validations(self, e):
        """validating the user inputs here for the system"""
        if not self.first_name.value:
            self.first_name.error_text = "fill in the blanks".title()
            self.first_name.error_style = ft.TextStyle(size=10)
            self.update()
        #  ----------------------getting the input values here for the lecture----------------//
        elif not self.last_name.value:
            self.last_name.error_text = "fill in the blanks".title()
            self.last_name.error_style = ft.TextStyle(size=10)
            self.update()
            #  ----------------------getting the input values here for the lecture----------------//
        elif not self.age.value:
            self.age.error_text = "fill in the blanks".title()
            self.age.error_style = ft.TextStyle(size=10)
            self.update()
        #  ----------------------getting the input values here for the lecture----------------//
        elif not self.gender.value:
            self.gender.error_text = "fill in the blanks".title()
            self.gender.error_style = ft.TextStyle(size=10)
            self.update()
        #  ----------------------getting the input values here for the lecture----------------//
        elif not self.email.value:
            self.email.error_text = "fill in the blanks".title()
            self.email.error_style = ft.TextStyle(size=10)
            self.update()
        #  ----------------------getting the input values here for the lecture----------------//
        elif not self.department.value:
            self.department.error_text = "fill in the blanks".title()
            self.department.error_style = ft.TextStyle(size=10)
            self.update()
        #  ----------------------getting the input values here for the lecture----------------//
        elif not self.phone_number.value:
            self.phone_number.error_text = "fill in the blanks".title()
            self.phone_number.error_style = ft.TextStyle(size=10)
            self.update()
            #  ----------------------getting the input values here for the lecture----------------//
        elif not self.teaching_experience.value:
            self.teaching_experience.error_text = "fill in the blanks".title()
            self.teaching_experience.error_style = ft.TextStyle(size=10)
            self.update()
            #  ----------------------getting the input values here for the lecture----------------//
        else:
            self.register_lecture_details()

    #  --------------returning the controls here----------------//
    def build(self):
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
                            #  ------------------------the container for the profile cards--------------//
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                self.registered_lectures
                                            ]
                                        )
                                    ]
                                )
                            ),
                            #  ----------------the container for the form and other controls-----//
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=20),
                                bgcolor="#F2ECFF",
                                content=ft.Column(
                                    controls=[
                                        #  -----------------for the top labels and text--------//
                                        ft.Container(
                                            padding=ft.padding.only(left=20),
                                            content=ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        "lecture details".capitalize(),
                                                        style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                        color="#0050C1"
                                                    ),
                                                ]
                                            )
                                        ),
                                        #  --------------------for the main form controls--------//
                                        ft.Container(
                                            padding=ft.padding.only(left=20),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row([self.first_name, self.last_name]),
                                                    ft.Row([self.age, self.gender]),
                                                    ft.Row([self.email, self.department]),
                                                    ft.Row([self.phone_number, self.teaching_experience])
                                                ]
                                            )
                                        ),
                                        #  ------------------the container will keep the controls for the buttons-----//
                                        ft.Container(
                                            padding=ft.padding.only(left=20),
                                            margin=ft.margin.only(top=10),
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        on_click=self.input_validations,
                                                        bgcolor="#007BDD",
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.SAVE_ROUNDED,
                                                                    size=20,
                                                                    color="white"),
                                                                ft.Text(
                                                                    "save lecture details".title(),
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
                            )
                        ]
                    )
                )
            ]
        )

    #  --------------------saving the lecture details function will be down here----------//
    def register_lecture_details(self):
        try:
            lecture = Lecture(
                self.first_name.value,
                self.last_name.value,
                self.age.value,
                self.gender.value,
                self.email.value,
                self.department.value,
                self.phone_number.value,
                self.teaching_experience.value,
            )
            lecture.save_lecture_details()
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

    #  ---------------method to clear text-boxes-------------------------//
    def clear_text_boxes(self):
        try:
            self.first_name.value = ""
            self.last_name.value = ""
            self.age.value = ""
            self.department.value = ""
            self.teaching_experience.values = ""
            self.phone_number.values = ""
            self.email.values = ""
            self.update()

        except Exception as ex:
            print(ex)

    def display_registered_record(self):
        try:
            sql = "SELECT * FROM lecture LIMIT 4"
            database_cursor = my_connection.cursor()
            database_cursor.execute(sql)
            all_results = database_cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in database_cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]

            for self.single_record in rows:
                self.registered_lectures.controls.append(
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
                                                                f"{self.single_record['first_name']}".capitalize(),
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

