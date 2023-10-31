import flet as ft
import os


class Gallery(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.LETTER_DATA_PATH = "C:/FinalProject/gallery/letters"
        self.NUMBER_DATA_PATH = "C:/FinalProject/gallery/numbers"
        self.Images = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            expand=1,
            wrap=True,
            scroll=ft.ScrollMode.ALWAYS
        )
        self.Numbers = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            expand=1,
            wrap=True,
            scroll=ft.ScrollMode.ALWAYS
        )

    def letters_gallery(self):
        try:
            for image_class in os.listdir(self.LETTER_DATA_PATH):
                self.Images.controls.append(
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(
                                    src=f"{self.LETTER_DATA_PATH}/{image_class}",
                                    width=300,
                                    height=300,
                                    fit=ft.ImageFit.COVER,
                                    border_radius=ft.border_radius.all(10),
                                )
                            ]
                        )
                    )
                )
        except Exception as ex:
            print(ex)

    #  -----------------the numbers gallery here----------------------//
    def numbers_gallery(self):
        try:
            for image_class in os.listdir(self.NUMBER_DATA_PATH):
                self.Numbers.controls.append(
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(
                                    src=f"{self.NUMBER_DATA_PATH}/{image_class}",
                                    width=300,
                                    height=300,
                                    fit=ft.ImageFit.COVER,
                                    border_radius=ft.border_radius.all(10),
                                )
                            ]
                        )
                    )
                )
        except Exception as ex:
            print(ex)

    def build(self):
        self.letters_gallery()
        self.numbers_gallery()
        return ft.ListView(
            controls=[
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(bottom=30),
                    margin=ft.margin.only(right=20),
                    bgcolor="#F2ECFF",
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
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
                                                                    ft.icons.SIGN_LANGUAGE_ROUNDED,
                                                                ),
                                                                ft.Text(
                                                                    "alphabet letters".title(),
                                                                    weight=ft.FontWeight.W_700
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    content=ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                self.Images
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
                                                                    ft.icons.SIGN_LANGUAGE_ROUNDED,
                                                                ),
                                                                ft.Text(
                                                                    "counter numbers".title(),
                                                                    weight=ft.FontWeight.W_700
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    content=ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                self.Numbers
                                                            ]
                                                        )
                                                    ),
                                                ),
                                            ],
                                            width=1100,
                                            height=700
                                        )
                                    ]
                                )
                            ),

                        ]
                    )
                )
            ]
        )
