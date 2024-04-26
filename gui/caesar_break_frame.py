import customtkinter as ctk
import tkinter as tk

from cipher.break_caesar import decrypt_caesar
from gui.gui_elements import create_tabs_encrypt_decrypt, configure_tab, setup_io_column_from_tab, \
    setup_output_break_column_tab, setup_options_break
from utils.file_utils import open_from_file, save_to_file
from utils.string_utils import get_validated_message, is_valid_string_key


class BreakCaesarCipherFrame(ctk.CTkFrame):
    def __init__(self, parent, load_main_menu):
        super().__init__(parent, fg_color='transparent')

        string_key = ctk.StringVar()
        checkbox_state = tk.BooleanVar()
        checkbox_state.set(False)
        self.entry_widget = None
        dinamic_content_frame = None

        break_caesar_notebook = create_tabs_encrypt_decrypt(self)
        break_caesar_notebook.pack(fill='both', expand=True, )
        break_tab = break_caesar_notebook.add('Break Caesar Cipher')
        configure_tab(break_tab)
        input_textbox, input_error = setup_io_column_from_tab(break_tab, "Encrypted message",
                                                              "Load file", open_from_file, column=0)
        output_textbox, cipher_textbox, output_error = setup_output_break_column_tab(break_tab, "Result message",
                                                                                     "Save to file",
                                                                                     save_to_file, column=2)
        setup_options_break(break_tab, string_key, checkbox_state, self.clear_tab, input_textbox, input_error,
                            output_textbox, cipher_textbox, output_error, self.on_checkbox_change,
                            dinamic_content_frame, self, load_main_menu, self.process_message)

    @staticmethod
    def process_message(self, input_txt, output_txt, alphabet, key, error_label):
        error_label.configure(text='')
        string_key = None

        content = input_txt.get("1.0", "end-1c")
        if not content.strip():
            error_label.configure(text='provide a message as input')
            return

        if self.entry_widget is not None:
            if not key:
                error_label.configure(text='invalid key')
                return

            if not is_valid_string_key(key):
                error_label.configure(text='invalid string key')
                return

            string_key = key.upper().replace(' ', '')

        message = get_validated_message(input_txt.get("1.0", "end-1c"))

        if string_key:
            result_message, result_alphabet = decrypt_caesar(message, string_key)
        else:
            result_message, result_alphabet = decrypt_caesar(message)

        output_txt.configure(state="normal")
        output_txt.delete("1.0", tk.END)
        output_txt.insert(tk.END, result_message)
        output_txt.configure(state="disabled")

        alphabet.configure(state="normal")
        alphabet.delete("1.0", tk.END)
        alphabet.insert(tk.END, result_alphabet)
        alphabet.configure(state="disabled")

    @staticmethod
    def clear_tab(input_txt, input_err, output_mess_txt, output_alph_txt, output_err, checkbox_state):
        input_txt.delete("1.0", tk.END)
        output_mess_txt.configure(state="normal")
        output_mess_txt.delete("1.0", tk.END)
        output_mess_txt.configure(state="disabled")
        output_alph_txt.configure(state="normal")
        output_alph_txt.delete("1.0", tk.END)
        output_alph_txt.configure(state="disabled")
        checkbox_state.set(False)
        input_err.configure(text='')
        output_err.configure(text='')
        pass

    @staticmethod
    def on_checkbox_change(self, checkbox_state, frame, var):
        if checkbox_state.get():
            if self.entry_widget is None:
                self.entry_widget = ctk.CTkEntry(frame, fg_color="#c4c4c4", width=190, font=("Arial", 16),
                                                 text_color='black', textvariable=var)
                self.entry_widget.pack(pady=(10, 0))
        else:
            if self.entry_widget is not None:
                self.entry_widget.destroy()
                self.entry_widget = None
