import flet as ft
import string
import openai
from time import sleep
import random

openai.api_key = open("pages/Api.txt", "r").read().strip("\n")


class Dictionary(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page = page
        self.image_url = ""
        self.numbers = random.randint(0, 9)
        self.letters = string.ascii_letters
        self.letter_blocks = ft.Text()
        self.message_history = []
        #   --------------building the variable for the model class here----------//

        self.word = ft.TextField(
            width=700,
            hint_text="enter dome text".capitalize(),
            label="support",
            border_color="white",
            focused_color="white",
            autofocus=True,
            prefix_icon=ft.icons.MODE_EDIT_ROUNDED,
            helper_text="get all information for starters".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
        )
        self.dictionary_words = ft.GridView(
            expand=1,
            runs_count=6,
            max_extent=70,
            child_aspect_ratio=0.9,
            spacing=1,
            run_spacing=5,
            padding=30,
            width=300,
        )

        #  -------------------the grid control for the numbers here-------------------//
        self.dictionary_numbers = ft.GridView(
            expand=1,
            runs_count=6,
            max_extent=70,
            child_aspect_ratio=0.9,
            spacing=1,
            run_spacing=5,
            padding=30,
            width=300,
        )
        #  --------------------//--------------------the numbers---------------------//
        self.progress = ft.ProgressBar(
            width=400,
        )

    def show_progress(self):
        for i in range(0, 101):
            self.progress.value = i * 0.01
            sleep(0.1)
            self.page.update()

    def validate_input(self, e):
        try:
            if not self.word.value:
                self.word.error_text = "enter a word please".title()
                self.page.update()
        except Exception as ex:
            print(ex)

    def on_click(self, e):
        self.letter_blocks = e.control.data
        dictionary_dialog = ft.AlertDialog(
            content=ft.Container(
                width=500,
                height=300,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            f"{self.letter_blocks}"
                        )
                    ]
                )
            )
        )
        self.page.dialog = dictionary_dialog
        dictionary_dialog.open = True
        self.page.update()

    def alphabet_letters(self):
        try:
            for letter in self.letters:
                self.dictionary_words.controls.append(
                    ft.Card(
                        elevation=1.0,
                        content=ft.Container(
                            data=letter,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(f"{letter}", size=30, weight=ft.FontWeight.W_500, color="#212121")]
                                    )
                                ]
                            ),
                            on_click=self.generate_ai_images
                        )
                    )
                )

        except Exception as ex:
            print(ex)

        #   --------------the function to generate the images here------------------//

    def generate_ai_images(self, e):
        try:
            entered_text = e.control.data
            response = openai.Image.create(
                prompt="sign language for {}".format(entered_text),
                n=1,
                size="512x512"
            )
            self.image_url = response['data'][0]['url']
            image_dialog = ft.AlertDialog(
                title=ft.Text(
                    "generated sign".title(),
                    style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                    weight=ft.FontWeight.W_500,
                ),
                title_padding=ft.padding.only(left=10, top=10),
                content=ft.Container(
                    content=ft.Column(
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            ft.Image(
                                src=self.image_url,
                                border_radius=ft.border_radius.all(10),
                            ),
                            #    -----------------the container that will generate the images-----/
                            ft.Container(
                                padding=ft.padding.only(bottom=10),
                                content=ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            on_click={},
                                            bgcolor="#007BDD",
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(ft.icons.REFRESH_ROUNDED, size=20,
                                                            color="white"),
                                                    ft.Text(
                                                        "close modal".title(),
                                                        color="white"
                                                    )
                                                ],

                                            ),
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),

            )
            self.page.dialog = image_dialog
            image_dialog.open = True
            self.page.update()
            self.clear_text()
        except Exception as ex:
            print(ex)

    def clear_text(self):
        try:
            self.word.value = ""
            self.page.update()
        except Exception as ex:
            print(ex)

    #   ------------------------chat generation-------------------------------//
    def generate_chart_responses(self, e):
        try:
            self.message_history.append({"role": "user", "content": self.word.value})
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                messages=self.message_history,
                temperature=0.7
            )
            results = completion.choices[0].message.content
            results_dlg = ft.AlertDialog(
                title=ft.Text(
                    "your generated response",
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color="#1565C0"
                ),
                content=ft.Container(
                    width=700,
                    content=ft.Column(
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            ft.Text(
                                f"{results}",
                                size=19,
                                weight=ft.FontWeight.W_500,
                                color="#212121"
                            )
                        ]
                    )
                )
            )
            self.page.dialog = results_dlg
            results_dlg.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    def build(self):
        self.alphabet_letters(),
        self.generate_random_numbers()
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=700,
            scale=1.0,
            controls=[
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                    margin=ft.margin.only(right=20, top=30),
                    bgcolor="#f5f5f5",
                    content=ft.Column(
                        controls=[
                            #   -----------------//------------------------//
                            #   ---------------------the container will be used to keep the introductory information---------//
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        #  ---------------------the other controls will be here---------//
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
                                                            width=800,
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
                                                                    ft.Container(
                                                                        margin=ft.margin.only(top=10),
                                                                        content=ft.Column(
                                                                            controls=[
                                                                                ft.Row([self.word]),
                                                                                ft.Row([
                                                                                    ft.ElevatedButton(
                                                                                        on_click=self.generate_chart_responses,
                                                                                        bgcolor="#007BDD",
                                                                                        content=ft.Row(
                                                                                            controls=[
                                                                                                ft.Icon(
                                                                                                    ft.icons.EDIT_NOTE_ROUNDED,
                                                                                                    size=20,
                                                                                                    color="white"),
                                                                                                ft.Text(
                                                                                                    "get support".title(),
                                                                                                    color="white"
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ])
                                                                            ]
                                                                        )
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            )
                                        ),

                                        #  ---------------------the second card for the page------------------//
                                        ft.Card(
                                            content=ft.Container(
                                                width=230,
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
                                                        ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.FLARE_ROUNDED,
                                                                    size=50,
                                                                    color="white"
                                                                )
                                                            ]
                                                        ),
                                                        #  -------------the list tile for the instructions-------//
                                                        ft.Container(
                                                            padding=ft.padding.only(bottom=20),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.ListTile(
                                                                        leading=ft.Icon(ft.icons.CHECKLIST_ROUNDED,
                                                                                        color="white"),
                                                                        title=ft.Text(
                                                                            "read one chapter of a book about sign languages".capitalize(),
                                                                            color="white"
                                                                        ),
                                                                        selected=True,

                                                                    ),
                                                                    ft.ListTile(
                                                                        leading=ft.Icon(ft.icons.CHECKLIST_ROUNDED,
                                                                                        color="white"),
                                                                        title=ft.Text(
                                                                            "sign up for sign language courses".capitalize(),
                                                                            color="white"
                                                                        ),
                                                                        selected=True,
                                                                    ),
                                                                    ft.ListTile(
                                                                        leading=ft.Icon(ft.icons.CHECKLIST_ROUNDED,
                                                                                        color="white"),
                                                                        title=ft.Text(
                                                                            "listen to podcats".capitalize(),
                                                                            color="white"
                                                                        ),
                                                                        selected=True,
                                                                    ),
                                                                    ft.ListTile(
                                                                        leading=ft.Icon(ft.icons.CHECKLIST_ROUNDED,
                                                                                        color="white"),
                                                                        title=ft.Text(
                                                                            "take lesson with a tutor three"
                                                                            "times a week".capitalize(),
                                                                            color="white"
                                                                        ),
                                                                        selected=True,
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
                            #   ------------------------the control for the container---------------//
                            #  ----------------------the dictionary will be here------------------//

                        ]
                    )
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Tabs(
                                scrollable=True,
                                animation_duration=9,
                                animate_size=300,
                                selected_index=0,
                                tabs=[
                                    ft.Tab(
                                        tab_content=ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.KEYBOARD_ALT_ROUNDED,
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
                                                    self.dictionary_words
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
                                                        ft.icons.KEYBOARD_ALT_ROUNDED,
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
                                                    self.dictionary_numbers
                                                ]
                                            )
                                        ),
                                    ),
                                ],
                                width=1100,
                                height=400
                            )
                        ]
                    )
                )
            ]
        )

    #  ------------------the function to generate the numbers will be here-----------------//
    def generate_random_numbers(self):
        try:
            for number in range(0, 20):
                self.dictionary_numbers.controls.append(
                    ft.Card(
                        elevation=1.0,
                        content=ft.Container(
                            data=number,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(f"{number}", size=30, weight=ft.FontWeight.W_500, color="#212121")]
                                    )
                                ]
                            ),
                            on_click=self.generate_ai_images
                        )
                    )
                )
        except Exception as ex:
            print(ex)
