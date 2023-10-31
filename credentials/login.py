import flet as ft
import json


class Login(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.ListView(
            controls=[
                ft.Text("login page"),
                ft.ElevatedButton(
                    on_click=lambda _: self.page.go("/main"),
                    text="home"
                )
            ]
        )
