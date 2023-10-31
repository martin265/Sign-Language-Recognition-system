import flet as ft
from connection.db import my_connection
from facial_recognition.collect_images import CollectStudentImage
import os
from PIL import Image
from classes.student import Student


class Students(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.student_image_capture = CollectStudentImage()
        self.DATA_PATH = "C:/FinalProject/data"
        #  ---------------getting input from the student----------------------//
        self.first_name = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="first name".capitalize(),
            hint_text="first name".capitalize(),
            autofocus=True,
            prefix_icon=ft.icons.PERSON_4_ROUNDED,
            helper_text="student first name".capitalize(),
        )
        #  --------------------------//---------------------------------------//
        self.last_name = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="last name".capitalize(),
            hint_text="last name".capitalize(),
            autofocus=True,
            prefix_icon=ft.icons.PERSON_4_ROUNDED,
            helper_text="student last name".capitalize(),
        )
        #  --------------------------//---------------------------------------//
        self.age = ft.TextField(
            width=500,
            border_color="#0050C1",
            label="age".capitalize(),
            hint_text="age".capitalize(),
            autofocus=True,
            prefix_icon=ft.icons.FORMAT_LIST_NUMBERED_RTL_ROUNDED,
            helper_text="age".capitalize(),
        )
        #  --------------------------//---------------------------------------//
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
        #  ----------------//-----------------------------//--------------------//
        self.grade = ft.Dropdown(
            label="select grade....",
            width=500,
            hint_text="required field",
            helper_text="only characters",
            border_color="#0050C1",
            prefix_icon=ft.icons.GRADE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("Level 4"),
                ft.dropdown.Option("Level 5"),
                ft.dropdown.Option("Level 6")
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
            focused_border_color="#1a237e", focused_color="#6200ea"
        )
        self.address = ft.TextField(
            width=500,
            label="enter your address...",
            hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.LOCATION_ON_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea"
        )
        self.course = ft.Dropdown(
            label="select course....",
            hint_text="required field",
            helper_text="only characters",
            prefix_icon=ft.icons.LIBRARY_BOOKS_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            width=500,
            options=[
                ft.dropdown.Option("Mathematics"),
                ft.dropdown.Option("Social Studies"),
                ft.dropdown.Option("Biology"),
                ft.dropdown.Option("Physical science"),
                ft.dropdown.Option("Geography"),
            ]
        )
        #  ------------------for the grid controls here------------------//
        self.image_gallery = ft.GridView(
            expand=1,
            runs_count=6,
            max_extent=300,
            child_aspect_ratio=0.9,
            spacing=1,
            run_spacing=5,
            padding=30,
            width=300,
        )

    #  -----------------------------the form details for the student will be here-----------------//
    def validate_data(self, e):
        #  --------------------------//----------------------------//
        if not self.first_name.value:
            self.first_name.error_text = "please fill in the first name"
            self.update()
        #  --------------------------//----------------------------//
        elif not self.last_name.value:
            self.last_name.error_text = "fill in for last name"
            self.update()
        #  --------------------------//----------------------------//
        elif not self.age.value:
            self.age.error_text = "fill in for last_name"
            self.update()
        #  --------------------------//----------------------------//
        elif not self.gender.value:
            self.gender.error_text = "fill in for gender"
            self.page.update()
        #  --------------------------//----------------------------//
        elif not self.grade.value:
            self.grade.error_text = "fill in for grade"
            self.update()
        #  --------------------------//----------------------------//
        elif not self.phone_number.value:
            self.phone_number.error_text = "fill in for phone number"
            self.update()
        #  --------------------------//----------------------------//
        elif not self.address.value:
            self.address.error_text = "add your address"
            self.update()
        #  --------------------------//----------------------------//
        elif not self.course.value:
            self.course.error_text = "add course"
            self.update()
        #  --------------------------//----------------------------//
        else:
            self.save_students_record()
            self.trigger_open_cv_camera()

    #  ------------the function to open the camera here------------//

    def trigger_open_cv_camera(self):
        try:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "your camera will open up soon".title(),
                                weight=ft.FontWeight.W_700,
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                color="white"
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.student_image_capture.collect_student_image(self.first_name.value)
        except Exception as ex:
            print(ex)

    def showing_images(self):
        for folder_name in os.listdir(self.DATA_PATH):
            for img in os.listdir(os.path.join(self.DATA_PATH, folder_name)):
                self.image_gallery.controls.append(
                    ft.Container(
                        margin=ft.margin.only(bottom=10),
                        width=300,
                        height=400,
                        border_radius=ft.border_radius.all(10),
                        bgcolor="#F2ECFF",
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(top=20),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Image(
                                                width=200,
                                                height=200,
                                                fit=ft.ImageFit.COVER,
                                                repeat=ft.ImageRepeat.NO_REPEAT,
                                                border_radius=ft.border_radius.all(10),
                                                src=f"data/{folder_name}/{img}",
                                            )
                                        ]
                                    )
                                ),
                                #  ---------------------the container for the information and buttons---------//
                                ft.Container(
                                    padding=ft.padding.only(left=10, bottom=30),
                                    margin=ft.margin.only(left=10, bottom=30),
                                    content=ft.Column(
                                        controls=[
                                            ft.IconButton(
                                                data=folder_name,
                                                icon=ft.icons.EXPAND_ROUNDED,
                                                icon_size=20,
                                                icon_color="white",
                                                bgcolor="#009CDC",
                                                tooltip="expand".title(),
                                                on_click=self.on_click
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )

    #   -----------------------the function to trigger the camera here-----------------//
    def build(self):
        self.showing_images()
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=700,
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            #  -------------------the container to show the registered students---------//
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                self.image_gallery
                                            ]
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=10, top=10, bottom=30),
                                bgcolor="#F2ECFF",
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            padding=ft.padding.only(left=20),
                                            width=1000,
                                            content=ft.Column(
                                                controls=[
                                                    #  ---------------the rows for the text fields here-------//
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            ft.Text(
                                                                "register student".capitalize(),
                                                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                                weight=ft.FontWeight.W_500,
                                                                color="#0078D9"
                                                            ),
                                                            ft.ElevatedButton(
                                                                on_click=self.trigger_open_cv_camera,
                                                                bgcolor="#007BDD",
                                                                content=ft.Row(
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.BROADCAST_ON_HOME_ROUNDED,
                                                                            size=20,
                                                                            color="white"),
                                                                        ft.Text(
                                                                            "register student using facial".title(),
                                                                            color="white"
                                                                        )
                                                                    ],
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                    ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Row([self.first_name, self.last_name]),
                                                                ft.Row([self.age, self.gender]),
                                                                ft.Row([self.grade, self.phone_number]),
                                                                ft.Row([self.address, self.course]),

                                                                #  -----the container for the buttons here-------------//
                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        controls=[
                                                                            ft.ElevatedButton(
                                                                                on_click=self.validate_data,
                                                                                bgcolor="#007BDD",
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Icon(
                                                                                            ft.icons.BROADCAST_ON_HOME_ROUNDED,
                                                                                            size=20,
                                                                                            color="white"),
                                                                                        ft.Text(
                                                                                            "register student".title(),
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
                            )
                        ]
                    )
                )
            ]
        )

    #  ---------------the function to clear the input fields here-------------//
    def clear_text_fields(self):
        try:
            self.first_name.value = ""
            self.last_name.value = ""
            self.age.value = ""
            self.grade.value = ""
            self.course.values = ""
            self.phone_number.values = ""
            self.address.values = ""
            self.update()
        except Exception as ex:
            print(ex)

    #  --------------------------//---------------larger image----------------------//
    def on_click(self, e):
        try:
            student_name = e.control.data
            sql = f"SELECT * FROM students WHERE first_name = '{student_name}' "
            values = "maggie"
            cursor = my_connection.cursor()
            cursor.execute(sql)
            all_results = cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]
            #  ----------------looping through all the records here-------------//
            for single_record in rows:
                student_profile_page = ft.AlertDialog(
                    content=ft.Container(
                        padding=ft.padding.only(left=20, top=20),
                        border_radius=ft.border_radius.all(10),
                        bgcolor="white",
                        width=600,
                        height=500,
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"student profile details",
                                            weight=ft.FontWeight.BOLD,
                                            color="#009CDC",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,

                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"FIRST NAME: {single_record['first_name']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"LAST NAME: {single_record['last_name']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"AGE: {single_record['age']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"GENDER: {single_record['gender']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"GRADE: {single_record['grade']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"PHONE NUMBER: {single_record['phone_number']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"ADDRESS: {single_record['address']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            f"COURSE: {single_record['course']}",
                                            weight=ft.FontWeight.BOLD,
                                            color="black",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                ),

                            ]
                        )
                    )
                )
                self.page.dialog = student_profile_page
                student_profile_page.open = True
                self.page.update()

        except Exception as ex:
            print(ex)

    def save_students_record(self):
        try:
            student = Student(self.first_name.value, self.last_name.value, self.age.value, self.gender.value,
                              self.grade.value, self.phone_number.value, self.address.value, self.course.value)
            student.add_new_student_details()
            self.showing_images()
            #  ----------------displaying the snack bar here--------------//
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "record saved successfully"
                            )
                        ]
                    )
                ),
                action="okay"
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