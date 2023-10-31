import flet as ft
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


def Dashboard(page: Page):
    page.add(flet.Text("Dashboard", expand=True))
    page.update()


def Login(page: flet.Page):
    def start_new_page(e):
        p = subPage(target=main)  # ! This is the "subPage" class.
        p.start()  # ! This will run and start the second page.
    page.add(flet.ElevatedButton("start new page", on_click=start_new_page))
    page.update()


def main(page: flet.Page):
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
        trailing=ft.Container(
            margin=ft.margin.only(top=20),
            width=230,
            height=200,
            border_radius=ft.border_radius.all(10),
            content=ft.Column(
                controls=[
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.CHECKLIST_ROUNDED,
                                        color="black"),
                        title=ft.Text(
                            "listen to podcats".capitalize(),
                            color="black"
                        ),
                        selected=True,
                    ),
                ]
            )
        ),
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
                icon_content=ft.Icon(ft.icons.SUPPORT_AGENT_ROUNDED, size=30, color="#FF7A56"),
                label_content=ft.Text(
                    "dictionary".title(),
                    tooltip="braille",
                )
            ),
        ],
        on_change=destination_pages
    )
    page_selected_index()

    #   ----------------------calling function for the subject class----------------//
    # ---------------------------//--------------------------//-----------------//
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


if __name__ == "__main__":  # this is important
    flet.app(target=Login, assets_dir="assets")
