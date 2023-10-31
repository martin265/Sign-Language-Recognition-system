import flet as ft


class Header(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=1090,
                        border_radius=ft.border_radius.all(10),
                        padding=ft.padding.only(left=10, right=30, top=30, bottom=30),
                        margin=ft.margin.only(right=20),
                        bgcolor="#F2ECFF",
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                   content=ft.Row(
                                       alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                       controls=[
                                           ft.Container(
                                               content=ft.Row(
                                                   controls=[
                                                       ft.Text(
                                                           "sign language recognition".capitalize(),
                                                           style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                           weight=ft.FontWeight.W_700,
                                                           color="#0050C1"
                                                       ),
                                                   ]
                                               )
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
