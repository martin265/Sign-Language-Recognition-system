from flet_multi_page import subPage
import flet as ft
import random
import json
from pages.dictionary import Dictionary
from pages.students import Students
from pages.lectures import Lectures
from pages.courses import Courses
from pages.lesson import Lessons
from pages.subjects import Subjects
from pages.translator import Translator
from pages.braille import Braille
from pages.dashboard import Dashboard
from pages.gallery import Gallery
from flet import *
from flet_multi_page import subPage
import flet
from pages.reports import Reports


def second_target(page: flet.Page):  # ? This is the target function of the second page.
    page.theme_mode = "light"
    page.window_center()
    page.window_always_on_top = False
    page.fetch_page_details()
    page.padding = 0

    #  -------------------route changes here----------------//
    page.floating_action_button = ft.FloatingActionButton(
        bgcolor="#212121",
        width=100,
        on_click=lambda _: trigger_modal,
        content=ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    ft.Icon(
                        ft.icons.FLARE_ROUNDED,
                        size=30,
                        color="white"
                    ),
                    ft.Text(
                        "inside".title(),
                        color="white"
                    ),
                ]
            )
        )
    )
    instructions = ft.AlertDialog(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("hello world")
                ]
            )
        )
    )

    def trigger_modal():
        page.dialog = instructions
        instructions.open = True
        page.update()

    #   -----------------------the main navigation bar for the system will be here--------//
    #  -----------------------------lets all be alive and praise to our Lord(Jesus Christ)
    #  ------------------------lets do this------------------------------//
    #  --------------------------codec by martin unwell @ 6:20, 2023 the year of our lord----//
    # ! I did comment these
    all_pages = [
        Dashboard(page=page),
        Lectures(page=page),
        Students(page=page),
        Subjects(page=page),
        Courses(page=page),
        Lessons(page=page),
        Translator(page=page),
        Braille(page=page),
        Gallery(page=page),
        Dictionary(page=page),
        Reports(page=page)
    ]

    #  ----------------------the function for the destination pages---------------//
    def destination_pages(e):
        page_selected_index()

    # ----------------the function to navigate through the pages here------------//
    def page_selected_index():
        for index, single_page in enumerate(all_pages):
            single_page.visible = True if index == system_navigation_rail.selected_index else False
            page.update()

    system_navigation_rail = ft.NavigationRail(
        # --------------------the control page for the system will be here-------------//
        #  -------------------the trailing container here--------------------//
        leading=ft.FloatingActionButton(
            width=220,
            height=80,
            content=ft.Container(
                padding=ft.padding.all(10),
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.SIGN_LANGUAGE_ROUNDED, size=40, color="#0078D9"),
                        ft.Text(
                            "sochie technical".title(),
                            size=20,
                            weight=ft.FontWeight.BOLD
                        )
                    ]
                )
            )
        ),
        width=250,
        # ------------------the other controls here--------------//
        selected_index=0,
        group_alignment=-0.9,
        min_width=80,
        bgcolor="#F2ECFF",
        extended=True,
        label_type=ft.NavigationRailLabelType.ALL,
        min_extended_width=250,
        #  -----------------------the navigationRail destinations-----------------//
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SPACE_DASHBOARD_ROUNDED, size=30, color="#0057CA", tooltip="lectures", ),
                label_content=ft.Text(
                    "dashboard".title(),
                    tooltip="dashboard",
                ),
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.MENU_BOOK_ROUNDED, size=30, color="#0057CA", tooltip="lectures", ),
                label_content=ft.Text(
                    "lectures".title(),

                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PEOPLE_ROUNDED, size=30, color="#212121", tooltip="students", ),
                label_content=ft.Text(
                    "students".title(),

                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SUBJECT_ROUNDED, size=30, color="#00CDAD", tooltip="subjects"),
                label_content=ft.Text(
                    "subjects".title(),

                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SCHOOL_ROUNDED, size=30, color="#E52E6A", tooltip="lesson", ),
                label_content=ft.Text(
                    "courses".title(),
                    tooltip="courses",
                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PLAY_LESSON_ROUNDED, size=30, color="#0057CA", tooltip="lesson", ),
                label_content=ft.Text(
                    "lessons".title(),

                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.G_TRANSLATE_ROUNDED, size=30, color="#B2128F", tooltip="translations"),
                label_content=ft.Text(
                    "translations".title(),
                    weight=ft.FontWeight.BOLD
                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.GRAIN_ROUNDED, size=30, color="#0057CA"),
                label_content=ft.Text(
                    "braille".title(),
                    tooltip="braille",
                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.IMAGE_ROUNDED, size=30, color="#311b92"),
                label_content=ft.Text(
                    "gallery".title(),
                    tooltip="gallery",
                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.ONLINE_PREDICTION_ROUNDED, size=30, color="#0050C1"),
                label_content=ft.Text(
                    "dictionary".title(),
                    tooltip="braille",
                )
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.REPORT_ROUNDED, size=30, color="#0050C1"),
                label_content=ft.Text(
                    "report".title(),
                    tooltip="braille",
                )
            ),
        ],
        on_change=destination_pages
    )
    page_selected_index()
    page.add(
        ft.Row(
            controls=[
                system_navigation_rail,
                ft.Column(all_pages, alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
    page.update()


def main(page: flet.Page):
    page.window_center()
    page.padding = 0
    page.theme_mode = "light"

    def start_new_page(e):
        p = subPage(target=second_target)  # ! This is the "subPage" class.
        p.start()  # ! This will run and start the second page.
        page.window_destroy()

    #  ----------------build controls for the login page here-----------------------//
    username = ft.TextField(
        width=500,
        border_color="#0050C1",
        label="username".title(),
        hint_text="select name",
        autofocus=True,
        helper_text="username".capitalize(),
        prefix_icon=ft.icons.PERSON_2_ROUNDED,
        focused_border_color="#1a237e",
        focused_color="#0050C1",
    )
    password = ft.TextField(
        width=500,
        border_color="#0050C1",
        label="password".title(),
        hint_text="select name",
        autofocus=True,
        helper_text="username".capitalize(),
        prefix_icon=ft.icons.PASSWORD_ROUNDED,
        focused_border_color="#1a237e",
        focused_color="#0050C1",
        password=True
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=start_new_page),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    #  -------------the login function here for the system--------------------//
    def login(e):
        if not username.value:
            username.error_text = "fill in the username".capitalize()
            page.update()
        elif not password.value:
            password.error_text = "enter your password".capitalize()
            page.update()
        else:
            f_username = username.value
            f_password = password.value
            with open("users.json", "r") as f:
                for line in f:
                    user = json.loads(line.strip())
                    if user["username"] == f_username and user["password"] == f_password:
                        page.dialog = dlg_modal
                        dlg_modal.open = True
                        page.update()
                        return
            page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "check your username and password"
                            )
                        ]
                    )
                )
            )
            page.snack_bar.open = True
            page.update()

    #  ------------------adding the page controls-------------------//
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=20, top=30),
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#0050C1",
                                        "#007BDD"
                                    ],
                                    begin=ft.alignment.bottom_left,
                                    end=ft.alignment.top_right
                                ),
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        "sochie technical college".title(),
                                                        style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                                        weight=ft.FontWeight.BOLD,
                                                        color="white"
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.Card(
                                            content=ft.Container(
                                                border_radius=ft.border_radius.all(10),
                                                gradient=ft.LinearGradient(
                                                    colors=[
                                                        "#00B4C6",
                                                        "#007BDD"
                                                    ],
                                                    begin=ft.alignment.bottom_left,
                                                    end=ft.alignment.top_right
                                                ),
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Container(
                                                            margin=ft.margin.only(top=20),
                                                            padding=ft.padding.only(left=200),
                                                            content=ft.Row(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                controls=[
                                                                    ft.Icon(
                                                                        ft.icons.MEDICAL_INFORMATION_ROUNDED,
                                                                        size=50,
                                                                        color="white"
                                                                    )
                                                                ]
                                                            )
                                                        ),
                                                        ft.Container(
                                                            padding=ft.padding.only(left=10, right=10),
                                                            margin=ft.margin.only(bottom=20),
                                                            width=600,
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text(
                                                                        "get information about sign langauge".title(),
                                                                        weight=ft.FontWeight.W_700,
                                                                        size=30,
                                                                        color="#212121",
                                                                    ),
                                                                    ft.Text(
                                                                        "Enter your idea and the system will "
                                                                        "respond your your request accordingly"
                                                                        ", machine"
                                                                        "learning and natural language"
                                                                        "processing. the content generated is "
                                                                        "proven to be of higher accuracy".title(),
                                                                        weight=ft.FontWeight.W_500,
                                                                        size=15,
                                                                        color="white"
                                                                    ),
                                                                    #  ---------------------the text boxes for creating the notes---//
                                                                ]
                                                            )
                                                        ),
                                                        ft.Container(
                                                            margin=ft.margin.all(10),
                                                            content=ft.Row(
                                                                expand=1, wrap=False, scroll=ft.ScrollMode.ALWAYS,
                                                                controls=[
                                                                    ft.Image(
                                                                        src=f"gallery/numbers/pexels-cottonbro-studio-4629624.jpg",
                                                                        width=200,
                                                                        height=200,
                                                                        fit=ft.ImageFit.COVER,
                                                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                                                        border_radius=ft.border_radius.all(10),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"gallery/numbers/pexels-cottonbro-studio-4629628.jpg",
                                                                        width=200,
                                                                        height=200,
                                                                        fit=ft.ImageFit.COVER,
                                                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                                                        border_radius=ft.border_radius.all(10),
                                                                    ),
                                                                    ft.Image(
                                                                        src=f"gallery/numbers/pexels-cottonbro-studio-4629633.jpg",
                                                                        width=200,
                                                                        height=200,
                                                                        fit=ft.ImageFit.COVER,
                                                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                                                        border_radius=ft.border_radius.all(10),
                                                                    ),
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            )
                                        ),
                                    ]
                                )
                            ),
                            #  -----------------the first container------------------//
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=20, top=30),
                                bgcolor="#f5f5f5",
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            margin=ft.margin.only(bottom=20, left=150),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.CircleAvatar(
                                                        foreground_image_url=f"https://images.pexels.com/photos/1366997/pexels-photo-1366997.jpeg?auto=compress&cs=tinysrgb&w=400",
                                                        height=200,
                                                        width=200,
                                                    ),
                                                ]
                                            )
                                        ),
                                        ft.Row([username]),
                                        ft.Row([password]),
                                        #  -----------------the login page for the system--------//
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        on_click=login,
                                                        bgcolor="#007BDD",
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.LOGIN_ROUNDED,
                                                                    size=20,
                                                                    color="white"),
                                                                ft.Text(
                                                                    "login".title(),
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
                            #  ----------------------the second container----------------//
                            ft.Container()
                            #  ------------------------------//------------------------//
                        ]
                    )
                ]
            )
        )
    )
    page.update()


if __name__ == "__main__":  # ? This is so important, there will be errors without it.
    flet.app(target=second_target, port=9090, assets_dir="assets")
