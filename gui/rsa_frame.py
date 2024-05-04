import customtkinter as ctk
import tkinter as tk

from cipher.rsa import check_p_q, generate_n, generate_euler_indicator, validate_e, mod_inverse, encrypt_character, \
    decrypt_character
from gui.gui_elements import create_tabs_encrypt_decrypt, configure_tab
from utils.int_utils import string_to_int_list


class RSAFrame(ctk.CTkFrame):
    def __init__(self, parent, load_main_menu):
        super().__init__(parent, fg_color='transparent')

        self.p = 0
        self.q = 0
        self.valid_p_q = False
        self.n = 0
        self.euler_n = 0
        self.e = 0
        self.d = 0
        self.are_keys_generated = False

        # encryption variables
        p_encrypt = ctk.StringVar()
        q_encrypt = ctk.StringVar()
        e_encrypt = ctk.StringVar()

        n_decrypt = ctk.StringVar()
        d_decrypt = ctk.StringVar()

        # create notebook
        double_key_notebook = create_tabs_encrypt_decrypt(self)
        double_key_notebook.pack(fill='both', expand=True, )

        # add tabs
        encrypt_tab = double_key_notebook.add('encrypt')
        decrypt_tab = double_key_notebook.add('decrypt')

        encrypt_keys_frame = ctk.CTkFrame(encrypt_tab, width=1300, height=300)
        encrypt_keys_frame.pack(expand=True, fill='both')

        for col in range(5):
            encrypt_keys_frame.columnconfigure(col, weight=1, uniform='group1')

        ctk.CTkLabel(encrypt_keys_frame, text="Enter p:").grid(column=0, row=0, padx=10, pady=(5, 0), sticky='ew')
        ctk.CTkLabel(encrypt_keys_frame, text="Enter q:").grid(column=0, row=2, padx=10, pady=(5, 0), sticky='ew')
        ctk.CTkLabel(encrypt_keys_frame, text="Enter e:").grid(column=2, row=0, padx=10, pady=(5, 0), sticky='ew')

        p_entry = ctk.CTkEntry(encrypt_keys_frame, textvariable=p_encrypt)
        p_entry.grid(column=0, row=1, padx=10, pady=5, sticky='ew')
        q_entry = ctk.CTkEntry(encrypt_keys_frame, textvariable=q_encrypt)
        q_entry.grid(column=0, row=3, padx=10, pady=5, sticky='ew')
        check_button = ctk.CTkButton(encrypt_keys_frame, text="Check Values",
                                     command=lambda: self.validate_p_q(p_encrypt.get(), q_encrypt.get(), p_q_error_label))
        check_button.grid(column=0, row=4, padx=10, pady=5, sticky='ew')
        p_q_error_label = ctk.CTkLabel(encrypt_keys_frame, text="Enter valid values for p and q")
        p_q_error_label.grid(column=0, row=5, padx=10, pady=(5, 0), sticky='ew')

        n_label = ctk.CTkLabel(encrypt_keys_frame, text="Find n")
        n_label.grid(column=1, row=0, padx=10, pady=(10, 0), sticky='ew')
        find_n_button = ctk.CTkButton(encrypt_keys_frame, text="Generate n",
                                      command=lambda: self.find_n(n_label, n_error_label))
        find_n_button.grid(column=1, row=1, padx=10, pady=20, sticky='ew')
        n_error_label = ctk.CTkLabel(encrypt_keys_frame, text="")
        n_error_label.grid(column=1, row=2, padx=10, pady=(5, 0), sticky='ew')

        euler_ind_label = ctk.CTkLabel(encrypt_keys_frame, text="Find the euler indicator")
        euler_ind_label.grid(column=1, row=3, padx=10, pady=(10, 0), sticky='ew')
        find_euler_button = ctk.CTkButton(encrypt_keys_frame, text="Generate euler indicator",
                                          command=lambda: self.find_euler_indicator(euler_ind_label, euler_error_label))
        find_euler_button.grid(column=1, row=4, padx=10, pady=20, sticky='ew')
        euler_error_label = ctk.CTkLabel(encrypt_keys_frame, text="")
        euler_error_label.grid(column=1, row=5, padx=10, pady=(5, 0), sticky='ew')

        e_entry = ctk.CTkEntry(encrypt_keys_frame, textvariable=e_encrypt)
        e_entry.grid(column=2, row=1, padx=10, pady=5, sticky='ew')
        check_e_button = ctk.CTkButton(encrypt_keys_frame, text="Check e value",
                                       command=lambda: self.validate_e(e_encrypt.get(), e_error_label))
        check_e_button.grid(column=2, row=2, padx=10, pady=5, sticky='ew')
        e_error_label = ctk.CTkLabel(encrypt_keys_frame, text="")
        e_error_label.grid(column=2, row=3, padx=10, pady=(5, 0), sticky='ew')

        d_label = ctk.CTkLabel(encrypt_keys_frame, text="Find d value")
        d_label.grid(column=3, row=0, padx=10, pady=(5, 0), sticky='ew')
        find_p_button = ctk.CTkButton(encrypt_keys_frame, text="Find d",
                                      command=lambda: self.find_d(d_label, d_error_label))
        find_p_button.grid(column=3, row=1, padx=10, pady=5, sticky='ew')
        d_error_label = ctk.CTkLabel(encrypt_keys_frame, text="")
        d_error_label.grid(column=3, row=2, padx=10, pady=(5, 0), sticky='ew')

        pk_sk_button = ctk.CTkButton(encrypt_keys_frame, text="Generate keys",
                                     command=lambda: self.find_keys(pk_encrypt_label, sk_encrypt_label))
        pk_sk_button.grid(column=3, row=4, padx=10, pady=5, sticky='ew')
        pk_encrypt_label = ctk.CTkLabel(encrypt_keys_frame, text="Public key will be displayed here",
                                        font=('Calibri', 15, 'bold'))
        pk_encrypt_label.grid(column=3, row=5, padx=10, pady=(5, 0), sticky='ew')
        sk_encrypt_label = ctk.CTkLabel(encrypt_keys_frame, text="Secret key will be displayed here",
                                        font=('Calibri', 15, 'bold'))
        sk_encrypt_label.grid(column=3, row=6, padx=10, pady=(5, 0), sticky='ew')

        clear_btn = ctk.CTkButton(encrypt_keys_frame, text="Clear tab", fg_color='red',
                                  command=lambda: self.clear_tab(p_entry, q_entry, p_q_error_label, n_label,
                                                                 n_error_label, euler_ind_label, euler_error_label,
                                                                 e_entry, e_error_label, d_label, d_error_label,
                                                                 sk_encrypt_label, pk_encrypt_label, message_to_encrypt,
                                                                 encrypted_message, encrypt_error))
        clear_btn.grid(column=4, row=3, padx=10, pady=5, sticky='ew')
        menu_btn = ctk.CTkButton(encrypt_keys_frame, text="Back to menu", fg_color='green',
                                 command=lambda: {self.clear_tab(p_entry, q_entry, p_q_error_label, n_label,
                                                                 n_error_label, euler_ind_label, euler_error_label,
                                                                 e_entry, e_error_label, d_label, d_error_label,
                                                                 sk_encrypt_label, pk_encrypt_label, message_to_encrypt,
                                                                 encrypted_message, encrypt_error),
                                                  load_main_menu('MainMenu')})
        menu_btn.grid(column=4, row=4, padx=10, pady=5, sticky='ew')

        encrypt_message_frame = ctk.CTkFrame(encrypt_tab, width=1300, height=200)
        encrypt_message_frame.pack(expand=True, fill='both', pady=(10, 10))

        encrypt_message_frame.columnconfigure(0, weight=4)
        encrypt_message_frame.columnconfigure(1, weight=2)
        encrypt_message_frame.columnconfigure(2, weight=4)

        ctk.CTkLabel(encrypt_message_frame, text="Message").grid(column=0, row=0, padx=10, pady=(5, 0), sticky='ew')
        ctk.CTkLabel(encrypt_message_frame, text="Encrypted message").grid(column=2, row=0, padx=10, pady=(5, 0), sticky='ew')

        message_to_encrypt = ctk.CTkTextbox(encrypt_message_frame, height=200, fg_color='#c4c4c4',
                                            text_color='black')
        message_to_encrypt.grid(column=0, row=1, padx=10, pady=(5, 0), sticky='ew')

        encrypted_message = ctk.CTkTextbox(encrypt_message_frame, height=200, fg_color='#c4c4c4',
                                           text_color='black', state='disabled')
        encrypted_message.grid(column=2, row=1, padx=10, pady=(5, 0), sticky='ew')

        encrypt_error = ctk.CTkLabel(encrypt_message_frame, text="")
        encrypt_error.grid(column=1, row=0, padx=10, pady=(5, 0), sticky='ew')

        encrypt_btn = ctk.CTkButton(encrypt_message_frame, text="Encrypt message",
                                    command=lambda:self.encrypt_message(message_to_encrypt, encrypted_message, encrypt_error))
        encrypt_btn.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

        # decrypt tab
        decrypt_tab.columnconfigure(0, weight=4)
        decrypt_tab.columnconfigure(1, weight=2)
        decrypt_tab.columnconfigure(2, weight=4)

        ctk.CTkLabel(decrypt_tab, text="Encrypted message", text_color='black').grid(column=0, row=0,
                                                                                     padx=10, pady=(5, 0), sticky='ew')
        ctk.CTkLabel(decrypt_tab, text="Decrypted message", text_color='black').grid(column=2, row=0,
                                                                                     padx=10, pady=(5, 0), sticky='ew')

        message_to_decrypt = ctk.CTkTextbox(decrypt_tab, height=500)
        message_to_decrypt.grid(column=0, row=1, padx=10, pady=(5, 0), sticky='ew')

        decrypted_message = ctk.CTkTextbox(decrypt_tab, height=500, state='disabled')
        decrypted_message.grid(column=2, row=1, padx=10, pady=(5, 0), sticky='ew')

        options_frame = ctk.CTkFrame(decrypt_tab, height=400, width=100, fg_color='transparent')
        options_frame.grid(column=1, row=1, padx=10, pady=(5, 0), sticky='ew')

        ctk.CTkLabel(options_frame, text="Enter n", text_color='black').pack(pady=(0, 10), fill='x')
        sk_n_entry = ctk.CTkEntry(options_frame, textvariable=n_decrypt)
        sk_n_entry.pack(pady=(0, 10), fill='x')

        ctk.CTkLabel(options_frame, text="Enter d", text_color='black').pack(pady=(10, 10), fill='x')
        sk_d_entry = ctk.CTkEntry(options_frame, textvariable=d_decrypt)
        sk_d_entry.pack(pady=(0, 10), fill='x')

        decrypt_btn = ctk.CTkButton(options_frame, text="Decrypt message",
                                    command=lambda: self.decrypt_message(message_to_decrypt, decrypted_message,
                                                                         decrypt_error, sk_n_entry.get(), sk_d_entry.get()))
        decrypt_btn.pack(pady=(0, 10), fill='x')

        decrypt_error = ctk.CTkLabel(options_frame, text="", text_color='black')
        decrypt_error.pack(pady=(0, 10), fill='x')

        decrypt_clear = ctk.CTkButton(options_frame, text="Clear",
                                      command=lambda: self.clear_decrypt(message_to_decrypt, decrypted_message,
                                                                         sk_n_entry, sk_d_entry, decrypt_error))
        decrypt_clear.pack(pady=(0, 10), fill='x')

        decrypt_main = ctk.CTkButton(options_frame, text="Load main menu",
                                     command=lambda: {self.clear_decrypt(message_to_decrypt, decrypted_message,
                                                                         sk_n_entry, sk_d_entry, decrypt_error),
                                                      load_main_menu('MainMenu')})
        decrypt_main.pack(pady=(0, 10), fill='x')

    def encrypt_message(self, input_txt, output_txt, error_label):
        error_label.configure(text="")

        if not self.are_keys_generated:
            error_label.configure(text="generate keys first")
            return

        content = input_txt.get("1.0", "end-1c")
        if not content.strip():
            error_label.configure(text='provide a message')
            return

        message = input_txt.get("1.0", "end-1c")
        chars = [encrypt_character(char, self.e, self.n) for char in message]
        output_txt.configure(state="normal")
        output_txt.delete("1.0", tk.END)
        output_txt.insert(tk.END, chars)
        output_txt.configure(state="disabled")

    def decrypt_message(self, input_txt, output_txt, error_label, n_str, d_str):
        error_label.configure(text="")

        try:
            n = int(n_str)
            d = int(d_str)
        except ValueError:
            error_label.configure(text="Invalid key values")
            return

        content = input_txt.get("1.0", "end-1c")
        if not content.strip():
            error_label.configure(text='provide a message')
            return

        int_list = string_to_int_list(content)
        decrypted_chars = [decrypt_character(value, d, n) for value in int_list]

        output_txt.configure(state="normal")
        output_txt.delete("1.0", tk.END)
        output_txt.insert(tk.END, decrypted_chars)
        output_txt.configure(state="disabled")

    def clear_tab(self, p_entry, q_entry, p_q_error, n_label, n_error, euler_label, euler_error, e_entry, e_error,
                  d_label, d_error, sk_label, pk_label, input_txt, output_txt, encrypt_err):
        self.p = 0
        self.q = 0
        self.valid_p_q = False
        self.n = 0
        self.euler_n = 0
        self.d = 0
        self.e = 0
        self.are_keys_generated = False

        p_entry.delete(0, "end")
        q_entry.delete(0, "end")
        e_entry.delete(0, "end")

        p_q_error.configure(text="")
        n_error.configure(text="")
        euler_error.configure(text="")
        e_error.configure(text="")
        d_error.configure(text="")
        encrypt_err.configure(text="")

        n_label.configure(text="Find n")
        euler_label.configure(text="Find the euler indicator")
        d_label.configure(text="Find d value")
        pk_label.configure(text="Public key will be displayed here")
        sk_label.configure(text="Secret key will be displayed here")

        input_txt.delete("1.0", tk.END)
        output_txt.configure(state="normal")
        output_txt.delete("1.0", tk.END)
        output_txt.configure(state="disabled")

    def clear_decrypt(self, input_txt, output_txt, key1, key2, error):
        key1.delete(0, "end")
        key2.delete(0, "end")
        error.configure(text="")

        input_txt.delete("1.0", tk.END)
        output_txt.configure(state="normal")
        output_txt.delete("1.0", tk.END)
        output_txt.configure(state="disabled")

    def find_n(self, n_label, error_label):
        if not self.valid_p_q:
            error_label.configure(text='Enter valid values for p and q')
            return

        n = generate_n(self.p, self.q)
        n_label.configure(text=f'n = {n}')
        error_label.configure(text='')
        self.n = n

    def find_d(self, d_label, error_label):
        if self.euler_n == 0 or self.e == 0:
            error_label.configure(text='find euler indicator and e')
            return

        d = mod_inverse(self.e, self.euler_n)

        if d == -1:
            error_label.configure(text='could not find d')
            return

        self.d = d
        d_label.configure(text=f'd = {d}')
        error_label.configure(text='')

    def find_euler_indicator(self, euler_label, error_label):
        if not self.valid_p_q or self.n == 0:
            error_label.configure(text='Enter valid values for p and q and n')
            return

        euler_indicator = generate_euler_indicator(self.p, self.q)
        euler_label.configure(text=f'euler indicator = {euler_indicator}')
        error_label.configure(text='')
        self.euler_n = euler_indicator

    def validate_p_q(self, p_str, q_str, error_label):
        try:
            p = int(p_str)
            q = int(q_str)
        except ValueError as e:
            error_label.configure(text='Invalid values for p or q')
            return

        if not check_p_q(p, q):
            error_label.configure(text='Invalid values for p or q')
            return
        else:
            self.p = p
            self.q = q
            self.valid_p_q = True
            error_label.configure(text='U can generate n')

    def validate_e(self, e_str, error_label):
        if not self.valid_p_q or self.n == 0:
            error_label.configure(text='Enter valid values for p and q and n')
            return

        try:
            e = int(e_str)
        except ValueError:
            error_label.configure(text='Invalid e value')
            return

        if not validate_e(e, self.euler_n):
            error_label.configure(text='Invalid e value')
            return

        error_label.configure(text='u can generate p')
        self.e = e

    def find_keys(self, pk_label, sk_label):
        if self.e == 0 or self.p == 0 or self.n == 0:
            pk_label.configure(text="cant generate pk")
            sk_label.configure(text="cant generate sk")
            return
        else:
            pk_label.configure(text=f"PK = [{self.e}, {self.n}]")
            sk_label.configure(text=f"SK = [{self.p}, {self.n}]")
            self.are_keys_generated = True
