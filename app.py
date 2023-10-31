import flet as ft
from credentials.login import Login
from main import main


class App(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.init()

    def init(self, ):
        self.page.on_route_change = self.on_route_change
        self.page.go("/login")

    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/main": main(self.page)
        }[self.page.route](self.page)

        self.page.views.clear(self.page)
        self.page.views.append(
            ft.View(route, [new_page])
        )


ft.app(target=App, view=ft.WEB_BROWSER)
