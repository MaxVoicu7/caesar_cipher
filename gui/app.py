import customtkinter as ctk

from gui.caesar_break_frame import BreakCaesarCipherFrame
from gui.main_menu_frame import MainMenuFrame
from gui.caesar_single_key_frame import CaesarSingleKeyFrame
from gui.caesar_double_key_frame import CaesarDoubleKeyFrame
from gui.rsa_frame import RSAFrame
from gui.vigenere_frame import VigenereFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('CRIPTOGTAPHY')
        self.iconbitmap('media/data-encryption.ico')
        self.configure(fg_color='#000')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        self.frames = {}
        self.current_frame = None

        self.init_ui()

    def init_ui(self):
        self.frames['MainMenu'] = MainMenuFrame(self, self.open_single_key_gui, self.open_double_key_gui,
                                                self.open_break_caesar, self.open_vigenere, self.open_rsa)
        self.frames['CaesarSingleKey'] = CaesarSingleKeyFrame(self, self.show_frame)
        self.frames['CaesarDoubleKey'] = CaesarDoubleKeyFrame(self, self.show_frame)
        self.frames['BreakCaesar'] = BreakCaesarCipherFrame(self, self.show_frame)
        self.frames['Vigenere'] = VigenereFrame(self, self.show_frame)
        self.frames['RSA'] = RSAFrame(self, self.show_frame)
        self.show_frame('MainMenu')

    def show_frame(self, name):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[name]
        self.current_frame.pack(expand=True)

    def open_single_key_gui(self):
        self.show_frame('CaesarSingleKey')

    def open_double_key_gui(self):
        self.show_frame('CaesarDoubleKey')

    def open_break_caesar(self):
        self.show_frame('BreakCaesar')

    def open_vigenere(self):
        self.show_frame('Vigenere')

    def open_rsa(self):
        self.show_frame('RSA')
