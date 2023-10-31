import os
import flet as ft


class BrailleConverter:
    """the class that will be used to transcribe the class braille dots"""

    def __init__(self):
        self.braille_dict = {
            'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
            'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
            'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
            's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
            'y': '⠽', 'z': '⠵', ' ': '⠀'
        }

    def generate_braille(self, text):
        braille_text = ''
        for char in text:
            braille_char = self.braille_dict.get(char.lower(), '')
            braille_text += braille_char

        return braille_text



