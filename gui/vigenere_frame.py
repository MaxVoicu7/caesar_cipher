import customtkinter as ctk
import tkinter as tk

from cipher.vigenere import vigenere_encryption, vigenere_decryption
from utils.string_utils import get_validated_message, is_valid_string_key
from gui.gui_elements import create_tabs_encrypt_decrypt, setup_io_column_from_tab, setup_options_column, configure_tab
from utils.file_utils import open_from_file, save_to_file


class VigenereFrame(ctk.CTkFrame):
    def __init__(self, parent, load_main_menu):
        super().__init__(parent, fg_color='transparent')

        # ctk variables
        key_encryption = ctk.StringVar()
        key_decryption = ctk.StringVar()

        # create notebook
        single_key_notebook = create_tabs_encrypt_decrypt(self)
        single_key_notebook.pack(fill='both', expand=True)

        # add tabs
        encrypt_tab = single_key_notebook.add('encrypt')
        decrypt_tab = single_key_notebook.add('decrypt')

        # encrypt tab
        configure_tab(encrypt_tab)
        encrypt_input_textbox, encrypt_input_error = setup_io_column_from_tab(encrypt_tab, "Message to be encrypted",
                                                                              "Load file", open_from_file, column=0)
        encrypt_output_textbox, encrypt_output_error = setup_io_column_from_tab(encrypt_tab, "Encrypted message",
                                                                                "Save to file", save_to_file, column=2)
        setup_options_column(
            encrypt_tab, key_encryption, self.process_message, self.clear_tab, encrypt_input_textbox,
            encrypt_output_textbox, encrypt_input_error, encrypt_output_error, load_main_menu,
            vigenere_encryption, operation_name="Encrypt")

        # decrypt tab
        configure_tab(decrypt_tab)
        decrypt_input_textbox, decrypt_input_error = setup_io_column_from_tab(decrypt_tab, "Encrypted message",
                                                                              "Load file", open_from_file, column=0)
        decrypt_output_textbox, decrypt_output_error = setup_io_column_from_tab(decrypt_tab, "Decrypted message",
                                                                                "Save to file", save_to_file, column=2)
        setup_options_column(
            decrypt_tab, key_decryption, self.process_message, self.clear_tab, decrypt_input_textbox,
            decrypt_output_textbox, decrypt_input_error, decrypt_output_error, load_main_menu,
            vigenere_decryption, operation_name="Decrypt")

    @staticmethod
    def process_message(input_textarea, output_textarea, key, error_label, function):
        error_label.configure(text='')

        content = input_textarea.get("1.0", "end-1c")
        if not content.strip():
            error_label.configure(text='provide a message as input')
            return

        if not key:
            error_label.configure(text='provide a key')
            return

        if not is_valid_string_key(key):
            error_label.configure(text='invalid string key')
            return

        message = get_validated_message(input_textarea.get("1.0", "end-1c"))
        validated_key = key.upper().replace(' ', '')
        processed_message = function(message, validated_key)
        output_textarea.configure(state="normal")
        output_textarea.delete("1.0", tk.END)
        output_textarea.insert(tk.END, processed_message)
        output_textarea.configure(state="disabled")

    @staticmethod
    def clear_tab(input_textarea, output_textarea, key_variable, error_encrypt, error_result):
        input_textarea.delete("1.0", tk.END)
        output_textarea.configure(state="normal")
        output_textarea.delete("1.0", tk.END)
        output_textarea.configure(state="disabled")
        key_variable.set('')
        error_encrypt.configure(text='')
        error_result.configure(text='')
