import customtkinter as ctk
from gui.gui_elements import create_menu_button


class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, parent, single_key_method, double_key_method):
        super().__init__(parent, fg_color='transparent')

        create_menu_button(self, 'Caesar cipher with one key', single_key_method, (0, 10))
        create_menu_button(self, 'Caesar cipher with two keys', double_key_method)
