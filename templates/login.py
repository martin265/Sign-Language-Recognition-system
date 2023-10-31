import flet as ft
from main import MainPage


class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.main = MainPage()

        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        on_click=lambda _: self.page.go(self.main.main(self.page))
                    )
                ]
            )
        )
        self.page.add(
            self.content
        )
        self.page.update()


if __name__ == "__main__":
    ft.app(target=Login)
