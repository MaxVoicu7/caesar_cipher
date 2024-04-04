import customtkinter as ctk
import tkinter as tk
from gui.gui_elements import create_tabs_encrypt_decrypt, configure_tab, setup_io_column_from_tab, \
    setup_options_column_two_keys
from utils.file_utils import open_from_file, save_to_file
from utils.int_utils import is_valid_key
from utils.string_utils import is_valid_string_key, get_validated_message
from cipher.caesar_double_key import caesar_double_key_encryption, caesar_double_key_decryption


class CaesarDoubleKeyFrame(ctk.CTkFrame):
    def __init__(self, parent, load_main_menu):
        super().__init__(parent, fg_color='transparent')

        # ctk variables for encrypt tab
        integer_key_encryption = ctk.StringVar()
        string_key_encryption = ctk.StringVar()

        # ctk variables for decrypt tab
        integer_key_decryption = ctk.StringVar()
        string_key_decryption = ctk.StringVar()

        # create notebook
        double_key_notebook = create_tabs_encrypt_decrypt(self)
        double_key_notebook.pack(fill='both', expand=True, )

        # add tabs
        encrypt_tab = double_key_notebook.add('encrypt')
        decrypt_tab = double_key_notebook.add('decrypt')

        # encrypt tab
        configure_tab(encrypt_tab)
        encrypt_input_textbox, encrypt_input_error = setup_io_column_from_tab(encrypt_tab, "Message to be encrypted",
                                                                              "Load file", open_from_file, column=0)
        encrypt_output_textbox, encrypt_output_error = setup_io_column_from_tab(encrypt_tab, "Encrypted message",
                                                                                "Save to file", save_to_file, column=2)
        setup_options_column_two_keys(
            encrypt_tab, integer_key_encryption, string_key_encryption, self.process_message, self.clear_tab,
            encrypt_input_textbox, encrypt_output_textbox, encrypt_input_error, encrypt_output_error, load_main_menu,
            caesar_double_key_encryption, operation_name="Encrypt")

        # decrypt tab
        configure_tab(decrypt_tab)

        decrypt_input_textbox, decrypt_input_error = setup_io_column_from_tab(decrypt_tab, "Encrypted message",
                                                                              "Load file", open_from_file, column=0)
        decrypt_output_textbox, decrypt_output_error = setup_io_column_from_tab(decrypt_tab, "Decrypted message",
                                                                                "Save to file", save_to_file, column=2)
        setup_options_column_two_keys(
            decrypt_tab, integer_key_decryption, string_key_decryption, self.process_message, self.clear_tab,
            decrypt_input_textbox, decrypt_output_textbox, decrypt_input_error, decrypt_output_error, load_main_menu,
            caesar_double_key_decryption, operation_name="Decrypt")

    @staticmethod
    def process_message(input_textarea, output_textarea, int_key, string_key, error_label, crypt_func):
        error_label.configure(text='')

        content = input_textarea.get("1.0", "end-1c")
        if not content.strip():
            error_label.configure(text='provide a message as input')
            return

        if not int_key or not string_key:
            error_label.configure(text='provide both keys')
            return

        if not is_valid_key(int_key):
            error_label.configure(text='invalid integer key')
            return

        if not is_valid_string_key(string_key):
            error_label.configure(text='invalid string key')
            return

        message = get_validated_message(input_textarea.get("1.0", "end-1c"))
        validated_str_key = string_key.upper().replace(' ', '')
        processed_message = crypt_func(message, int(int_key), validated_str_key)
        output_textarea.configure(state="normal")
        output_textarea.delete("1.0", tk.END)
        output_textarea.insert(tk.END, processed_message)
        output_textarea.configure(state="disabled")

    @staticmethod
    def clear_tab(input_textarea, output_textarea, int_variable, string_variable, error_encrypt, error_result):
        input_textarea.delete("1.0", tk.END)
        output_textarea.configure(state="normal")
        output_textarea.delete("1.0", tk.END)
        output_textarea.configure(state="disabled")
        int_variable.set('')
        string_variable.set('')
        error_encrypt.configure(text='')
        error_result.configure(text='')
