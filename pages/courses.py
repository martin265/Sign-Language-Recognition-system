import flet as ft
import openai
import docx

#  ----------------------the api call here------------------//
openai.api_key = open("pages/Api.txt", "r").read().strip("\n")


#  --------------------------//----------------------------//
class Courses(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.create_notes = ft.TextField(
            width=450,
            hint_text="enter your topic".capitalize(),
            label="study notes",
            border_color="white",
            focused_color="white",
            prefix_icon=ft.icons.MODE_EDIT_ROUNDED,
            label_style=ft.TextStyle(
                color="white"
            ),
            helper_text="enter your topic"
        )
        #   ------------------------the text-boxes for creating the sample questions----------------------------//
        self.create_questions = ft.TextField(
            width=450,
            hint_text="enter your topic".capitalize(),
            label="questions",
            border_color="white",
            focused_color="white",
            prefix_icon=ft.icons.MODE_EDIT_ROUNDED,
            helper_text="create questions",
            label_style=ft.TextStyle(
                color="white"
            ),
        )

        #   -----------------------------------the text field for grammar and languages------------------------//
        self.correct_grammar = ft.TextField(
            width=450,
            hint_text="enter some words".capitalize(),
            label="grammar",
            border_color="white",
            focused_color="white",
            prefix_icon=ft.icons.MODE_EDIT_ROUNDED,
            helper_text="correct grammar",
            label_style=ft.TextStyle(
                color="white"
            ),
        )
        #  ---------------------------------------//--------------------------------------------//
        self.translate_global = ft.TextField(
            width=450,
            hint_text="enter some words".capitalize(),
            label="questions",
            border_color="white",
            focused_color="white",
            prefix_icon=ft.icons.MODE_EDIT_ROUNDED,
            helper_text="translate to other languages",
            label_style=ft.TextStyle(
                color="white"
            ),
        )

    #  ------------------------------function to validate the input fields---------------------------//
    def validate_create_notes(self, e):
        try:
            if not self.create_notes.value:
                self.create_notes.error_text = "fill in the top".capitalize()
                self.update()
            else:
                self.create_notes_api()
        except Exception as ex:
            print(ex)

    #  ------------------------------function to validate the input fields---------------------------//
    def validate_create_questions(self, e):
        try:
            if not self.create_questions.value:
                self.create_questions.error_text = "fill in the top".capitalize()
                self.update()
            else:
                self.create_questions_api()
        except Exception as ex:
            print(ex)

    #  ---------------------------------//-----------------------function to trigger the api model here----------------//
    def create_notes_api(self):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{self.create_notes.value}",
                temperature=0.3,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            results = response.choices[0]['text']
            alert_model_notes = ft.AlertDialog(
                title=ft.Text(
                    "your generated notes".capitalize()
                ),
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"{results}", size=30, weight=ft.FontWeight.W_500)
                        ]
                    )
                )
            )
            print(results)
            #  -------------------showing the snack-bar first----------------//
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("your response will be generated soon".title()),
                action="okay".capitalize()
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.page.dialog = alert_model_notes
            alert_model_notes.open = True
            self.page.update()
            #  -----------------opening the snack bar here--------------------//
        except Exception as ex:
            print(ex)

    #  ---------------------------------//-----------------------function to trigger the api model here----------------//
    def create_questions_api(self):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=self.create_questions.value,
                temperature=0.5,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            questions_results = response.choices[0]['text']
            alert_model_notes = ft.AlertDialog(
                title=ft.Text(
                    "your generated questions".capitalize(),
                    size=30,
                    weight=ft.FontWeight.W_500
                ),
                title_padding=ft.padding.only(left=20),
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"{questions_results}", size=30, weight=ft.FontWeight.W_500),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            on_click=self.print_to_word_document,
                                            bgcolor="#007BDD",
                                            content=ft.Row(
                                                controls=[
                                                    ft.Icon(
                                                        ft.icons.SAVE_ROUNDED,
                                                        size=20,
                                                        color="white"),
                                                    ft.Text(
                                                        "print to pdf".capitalize(),
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
            )
            #  -------------------showing the snack-bar first----------------//
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("your response will be generated soon".title()),
                action="okay".capitalize()
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.page.dialog = alert_model_notes
            alert_model_notes.open = True
            self.page.update()
            #  -----------------opening the snack bar here--------------------//
        except Exception as ex:
            print(ex)

    def print_to_word_document(self, e):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{self.create_notes.value}",
                temperature=0.3,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            #  ------------------printing the document here-------------//
            questions_results = response.choices[0]['text']
            document = docx.Document()
            document.add_paragraph("hello world")
            document.save('assets/your_file_name.docx')
            #   -------------------------saving the generated text here-----------------//
        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=700,
            scale=1.0,
            controls=[
                #  ----------------------the container for the top page here---//
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                    margin=ft.margin.only(right=20, top=30),
                    bgcolor="#f5f5f5",
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
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
                                                                    ft.icons.SPEAKER_NOTES_ROUNDED,
                                                                    size=50,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=10),
                                                        margin=ft.margin.only(bottom=20),
                                                        width=500,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(
                                                                    "create study notes".title(),
                                                                    weight=ft.FontWeight.W_700,
                                                                    size=30,
                                                                    color="#212121",

                                                                ),
                                                                ft.Text(
                                                                    "provide a topic and the system will "
                                                                    "automatically create notes basing on the"
                                                                    "topic that you have provide using, machine"
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
                                                                            ft.Row([self.create_notes]),
                                                                            ft.Row([
                                                                                ft.ElevatedButton(
                                                                                    on_click=self.validate_create_notes,
                                                                                    bgcolor="#007BDD",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Icon(
                                                                                                ft.icons.EDIT_NOTE_ROUNDED,
                                                                                                size=20,
                                                                                                color="white"),
                                                                                            ft.Text(
                                                                                                "create notes".title(),
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

                                    #  -------------------------the second card for the page here---------------------//
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
                                                                    ft.icons.ADD_ROAD_ROUNDED,
                                                                    size=50,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=10),
                                                        margin=ft.margin.only(bottom=20),
                                                        width=500,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(
                                                                    "create questions".title(),
                                                                    weight=ft.FontWeight.W_700,
                                                                    size=30,
                                                                    color="#212121",

                                                                ),
                                                                ft.Text(
                                                                    "provide a topic and the system will "
                                                                    "automatically questions basing on the"
                                                                    "topic that you have provide using, machine"
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
                                                                            ft.Row([self.create_questions]),
                                                                            ft.Row([
                                                                                ft.ElevatedButton(
                                                                                    on_click=self.validate_create_questions,
                                                                                    bgcolor="#007BDD",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Icon(
                                                                                                ft.icons.EDIT_NOTE_ROUNDED,
                                                                                                size=20,
                                                                                                color="white"),
                                                                                            ft.Text(
                                                                                                "create question".title(),
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
                                ]
                            ),

                            #  ---------------------------the other row for the containers here----------------//
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Card(
                                        content=ft.Container(
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0096DD",
                                                    "#FF8566"
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
                                                                    ft.icons.CLOUD_SYNC_ROUNDED,
                                                                    size=50,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=10),
                                                        margin=ft.margin.only(bottom=20),
                                                        width=500,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(
                                                                    "grammar correction".title(),
                                                                    weight=ft.FontWeight.W_700,
                                                                    size=30,
                                                                    color="#212121",

                                                                ),
                                                                ft.Text(
                                                                    "enter your text and the system will "
                                                                    "automatically analyse basing on the"
                                                                    "topic that you have provide using, machine"
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
                                                                            ft.Row([self.correct_grammar]),
                                                                            ft.Row([
                                                                                ft.ElevatedButton(
                                                                                    on_click=self.validate_grammar_input,
                                                                                    bgcolor="#007BDD",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Icon(
                                                                                                ft.icons.EDIT_NOTE_ROUNDED,
                                                                                                size=20,
                                                                                                color="white"),
                                                                                            ft.Text(
                                                                                                "correct grammar".title(),
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

                                    #  -------------------------the second card for the page here---------------------//
                                    ft.Card(
                                        content=ft.Container(
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0096DD",
                                                    "#FF4697"
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
                                                                    ft.icons.LANGUAGE_ROUNDED,
                                                                    size=50,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=ft.padding.only(left=10, right=10),
                                                        margin=ft.margin.only(bottom=20),
                                                        width=500,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(
                                                                    "english to other languages".title(),
                                                                    weight=ft.FontWeight.W_700,
                                                                    size=30,
                                                                    color="#212121",

                                                                ),
                                                                ft.Text(
                                                                    "provide a some text and the system will "
                                                                    "automatically translate basing on the"
                                                                    "topic that you have provide using, machine"
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
                                                                            ft.Row([self.translate_global]),
                                                                            ft.Row([
                                                                                ft.ElevatedButton(
                                                                                    on_click=self.validate_translation_inputs,
                                                                                    bgcolor="#007BDD",
                                                                                    content=ft.Row(
                                                                                        controls=[
                                                                                            ft.Icon(
                                                                                                ft.icons.EDIT_NOTE_ROUNDED,
                                                                                                size=20,
                                                                                                color="white"),
                                                                                            ft.Text(
                                                                                                "translate".title(),
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
                                ]
                            ),
                        ]
                    )
                ),
                #   ---------------------the other container here-------------//

            ]
        )

    #  ----------------------the validations for the grammar and translations-------------//
    def validate_grammar_input(self, e):
        try:
            if not self.correct_grammar.value:
                self.correct_grammar.error_text = "add some words".capitalize()
                self.update()
            else:
                self.get_correct_grammar()
        except Exception as ex:
            print(ex)

    #  -----------------------------function to generate the correct grammar here---------------//
    def get_correct_grammar(self):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=self.correct_grammar.value,
                temperature=0,
                max_tokens=60,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            results = response.choices[0]['text']
            correct_grammar = ft.AlertDialog(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                f"{results}",
                                size=30,
                                weight=ft.FontWeight.W_500
                            )
                        ]
                    )
                )
            )
            self.page.dialog = correct_grammar
            correct_grammar.open = True
            self.page.update()
        except Exception as ex:
            print(ex)
    #  ---------------------------the function ends here----------------------------//

    def validate_translation_inputs(self, e):
        try:
            if not self.translate_global.value:
                self.translate_global.error_text = "add some words".capitalize()
                self.update()
            else:
                self.get_translated_text()
        except Exception as ex:
            print(ex)

    #  ------------------------function to get the translations here---------------------//
    def get_translated_text(self):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=self.translate_global.value,
                temperature=0.3,
                max_tokens=100,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            results = response.choices[0]['text']
            print(results)
            translations_page = ft.AlertDialog(
                content=ft.Container(
                    height=500,
                    width=700,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                f"{results}",
                                size=30,
                                weight=ft.FontWeight.W_500
                            )
                        ]
                    )
                )
            )
            self.page.dialog = translations_page
            translations_page.open = True
            self.page.update()

        except Exception as ex:
            print(ex)
