import flet as ft
#  -------------------importing the translation models here-------------------//
import pickle
from LettersModel.inference_classfier import LettersModelInference
import time
from FingersModel.inference_classfier import NumbersModel
from pages.Sign_language_detection.inference_classifier import AllSigns

POINTS = [
    (0, 273.60),
    (1, 279.00),
    (2, 348.20),
    (3, 363.70),
    (4, 438.40),
    (5, 518.90),
    (6, 638.00),
    (7, 833.75),
    (8, 874.75),
    (9, 1096.50),
    (10, 1226.75),
    (11, 1577.00),
    (12, 1668.75),
    (13, 1200.00),
    (14, 1184.75),
    (15, 1061.25),
    (16, 1151.00),
    (17, 1257.25),
    (18, 1301.50),
    (19, 1493.25),
    (20, 1906.25),
    (21, 1753.90),
    (22, 1980.40),
]

BTC = [
    (9, 0.0008),
    (10, 0.07),
    (11, 0.95),
    (12, 13.44),
    (13, 817.36),
    (14, 314.24),
    (15, 430.05),
    (16, 963.74),
    (17, 13880.74),
    (18, 3843.52),
    (19, 7191.68),
    (20, 29001.19),
    (21, 39800.00),
]


class State:
    toggle = True


s = State()


#   ---------------------the data from the chart here--------------//
class Translator(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.all_signs = AllSigns()
        #  ----------------------calling the model calls here------------//
        self.alphabet_letters = LettersModelInference()
        self.numbers_model = NumbersModel()
        self.model = pickle.load(open("./LettersModel/model.p", "rb"))
        self.data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(0, 3),
                    ft.LineChartDataPoint(2.6, 2),
                    ft.LineChartDataPoint(4.9, 5),
                    ft.LineChartDataPoint(6.8, 3.1),
                    ft.LineChartDataPoint(8, 4),
                    ft.LineChartDataPoint(9.5, 3),
                    ft.LineChartDataPoint(11, 4),
                ],
                stroke_width=1,
                color="#0078D9",
                curved=True,
                stroke_cap_round=True,
                below_line_gradient=ft.LinearGradient(
                    colors=[
                        ft.colors.with_opacity(0.56, "#0078D9"),
                        ft.colors.with_opacity(0.56, "#009CDC")
                    ],
                    begin=ft.alignment.bottom_left,
                    end=ft.alignment.top_right
                )
            )
        ]
        self.chart = ft.LineChart(
            data_series=self.data_1,
            # border=ft.border.all(1, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=15,
                        label=ft.Text("80%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=13,
                        label=ft.Text("70%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=11,
                        label=ft.Text("60%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=9,
                        label=ft.Text("50%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=7,
                        label=ft.Text("40%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Text("30%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Text("20%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Text("10%", size=14, weight=ft.FontWeight.BOLD),
                    ),
                ],
                labels_size=30,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Container(
                            ft.Text(
                                "DAY 1",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Container(
                            ft.Text(
                                "DAY 2",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=8,
                        label=ft.Container(
                            ft.Text(
                                "DAY 3",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=8,
                        label=ft.Container(
                            ft.Text(
                                "DAY 4",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
            min_y=0,
            max_y=6,
            min_x=0,
            max_x=11,
            # animate=5000,
            expand=True,
        )

    def toggle_data(self, e):
        if s.toggle:
            self.chart.data_series = self.data_1
            self.chart.interactive = False
        else:
            self.chart.data_series = self.data_1
            self.chart.interactive = True
        s.toggle = not s.toggle
        self.chart.update()

    #  ----------------------the function to start model number inference--------------//
    def start_numbers_inference(self, e):
        try:
            print("hello world")
        except Exception as ex:
            print(ex)

    #  -------------------------the function to start the model inference-------------//
    def start_alphabet_inference(self, e):
        try:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "your camera will start soon".title(),
                                size=30,
                                weight=ft.FontWeight.W_700,
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.alphabet_letters.letter_inference()
        except Exception as ex:
            print(ex)

    def start_numbers_inference(self, e):
        try:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "your camera will start soon".title(),
                                size=30,
                                weight=ft.FontWeight.W_700,
                                style=ft.TextThemeStyle.TITLE_MEDIUM
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.numbers_model.get_trained_numbers()
        except Exception as ex:
            print(ex)

    def get_all_signs_inference(self, e):
        self.page.snack_bar = ft.SnackBar(
            bgcolor="#0050C1",
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "the camera will open soon".capitalize(),
                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                            weight=ft.FontWeight.W_700,
                            color="white"
                        )
                    ]
                )
            )
        )
        self.page.snack_bar.open = True
        self.page.update()
        self.all_signs.start_inference()

    #  ----------------------the controls for the chart will be here for the system--------------//
    #  ----------------------the main function for the controls--------------//
    def build(self):

        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1200,
            height=800,
            scale=1.0,
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                border_radius=ft.border_radius.all(10),
                                padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                                margin=ft.margin.only(right=20, top=40),
                                bgcolor="#f5f5f5",
                                content=ft.Column(
                                    #  -----------------the container to house the inside containers
                                    controls=[
                                        #  ------------------the row will controls the cards-------//
                                        #  ----------------the first row----------//
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    padding=ft.padding.only(left=30),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Text(
                                                                "hand sign language translator".capitalize(),
                                                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                                color="#008CFF",
                                                                weight=ft.FontWeight.BOLD,
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ]
                                        ),
                                        #  ----------------------the last page for the controls here----------//
                                        ft.Container(
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            #  ------------------the first container here---------//
                                                            ft.Container(
                                                                width=330,
                                                                height=400,
                                                                margin=ft.margin.only(left=18, top=30),
                                                                border_radius=ft.border_radius.all(20),
                                                                gradient=ft.LinearGradient(
                                                                    colors=[
                                                                        "#00B4C6",
                                                                        "#007BDD"
                                                                    ],
                                                                    begin=ft.alignment.bottom_left,
                                                                    end=ft.alignment.top_right
                                                                ),
                                                                content=ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Row(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                controls=[
                                                                                    ft.Image(
                                                                                        src=f"assets/signs/pexels-kevin-malik-9017414 (1).jpg",
                                                                                        width=300,
                                                                                        height=300,
                                                                                        fit=ft.ImageFit.COVER,
                                                                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                                                                        border_radius=ft.border_radius.all(
                                                                                            10)
                                                                                    ),

                                                                                ]
                                                                            ),
                                                                            ft.Container(
                                                                                padding=ft.padding.only(left=20,
                                                                                                        top=10),
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.ElevatedButton(
                                                                                            text="translate numbers",
                                                                                            on_click=self.start_numbers_inference,
                                                                                            icon=ft.icons.NUMBERS_ROUNDED
                                                                                        )
                                                                                    ]
                                                                                )
                                                                            )

                                                                        ]
                                                                    )
                                                                )

                                                            ),
                                                            #  --------------------the second container in the ro------//
                                                            ft.Container(
                                                                width=330,
                                                                height=400,
                                                                margin=ft.margin.only(left=10, top=30),
                                                                border_radius=ft.border_radius.all(20),
                                                                gradient=ft.LinearGradient(
                                                                    colors=[
                                                                        "#0096DD",
                                                                        "#FF8566"
                                                                    ],
                                                                    begin=ft.alignment.bottom_left,
                                                                    end=ft.alignment.top_right
                                                                ),
                                                                content=ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Row(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                controls=[
                                                                                    ft.Image(
                                                                                        src=f"assets/signs/pexels-kevin-malik-9017748.jpg",
                                                                                        width=300,
                                                                                        height=300,
                                                                                        fit=ft.ImageFit.COVER,
                                                                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                                                                        border_radius=ft.border_radius.all(
                                                                                            10)
                                                                                    ),

                                                                                ]
                                                                            ),
                                                                            ft.Container(
                                                                                padding=ft.padding.only(left=20,
                                                                                                        top=10),
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.ElevatedButton(
                                                                                            text="translate alphabet letters",
                                                                                            on_click=self.start_alphabet_inference,
                                                                                            icon=ft.icons.SORT_BY_ALPHA_ROUNDED
                                                                                        )
                                                                                    ]
                                                                                )
                                                                            )

                                                                        ]
                                                                    )
                                                                )

                                                            ),

                                                            #  -----------------------the last container here----------//
                                                            ft.Container(
                                                                width=330,
                                                                height=400,
                                                                margin=ft.margin.only(left=10, top=30),
                                                                border_radius=ft.border_radius.all(20),
                                                                gradient=ft.LinearGradient(
                                                                    colors=[
                                                                        "#0096DD",
                                                                        "#FF4697"
                                                                    ],
                                                                    begin=ft.alignment.bottom_left,
                                                                    end=ft.alignment.top_right
                                                                ),
                                                                content=ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Row(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                controls=[
                                                                                    ft.Image(
                                                                                        src=f"assets/signs/pexels-cottonbro-studio-4629625.jpg",
                                                                                        width=300,
                                                                                        height=300,
                                                                                        fit=ft.ImageFit.COVER,
                                                                                        repeat=ft.ImageRepeat.NO_REPEAT,
                                                                                        border_radius=ft.border_radius.all(
                                                                                            10)
                                                                                    ),

                                                                                ]
                                                                            ),
                                                                            ft.Container(
                                                                                padding=ft.padding.only(left=20,
                                                                                                        top=10),
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.ElevatedButton(
                                                                                            text="both hands".capitalize(),
                                                                                            on_click=self.get_all_signs_inference,
                                                                                            icon=ft.icons.SIGN_LANGUAGE_ROUNDED
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
                                                    ft.Row()
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),

                #  ----------------------the chart container here for the system----------------//
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.only(left=10, right=10, top=30, bottom=30),
                    margin=ft.margin.only(right=20, top=10, bottom=40),
                    expand=True,
                    # gradient=ft.LinearGradient(
                    #     colors=[
                    #         "#00B4C6",
                    #         "#007BDD"
                    #     ]
                    # ),
                    height=500,
                    width=1000,
                    bgcolor="#f5f5f5",
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                on_click={},
                                bgcolor="#007BDD",
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.icons.BROADCAST_ON_HOME_ROUNDED,
                                            size=20,
                                            color="white"),
                                        ft.Text(
                                            "refresh".title(),
                                            color="white"
                                        )
                                    ],
                                ),
                            ),
                            self.chart
                        ]
                    )
                )
            ]
        )
