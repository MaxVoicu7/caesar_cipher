import customtkinter as ctk


# create button for main menu frame
def create_menu_button(parent, text, method, padding_y=(0, 0)):
    ctk.CTkButton(parent,
                  text=text,
                  width=350,
                  height=70,
                  corner_radius=15,
                  fg_color='white',
                  text_color='black',
                  font=('Calibri', 25, 'bold'),
                  hover_color='grey',
                  command=method
                  ).pack(pady=padding_y)


def create_tabs_encrypt_decrypt(parent):
    return ctk.CTkTabview(parent,
                          width=1400,
                          height=700,
                          anchor='nw',
                          text_color='black',
                          fg_color='white',
                          segmented_button_fg_color='gray',
                          segmented_button_selected_color='green',
                          segmented_button_unselected_color='gray')


def create_label(parent, text, text_color="black", font=("Arial", 20, 'bold')):
    label = ctk.CTkLabel(parent, text=text, text_color=text_color, font=font)
    return label


def create_textarea(parent, row, column, height=500, fg_color='#c4c4c4', text_color='black', state=None):
    textarea = ctk.CTkTextbox(parent, height=height, fg_color=fg_color, text_color=text_color, state=state)
    textarea.grid(row=row, column=column, sticky="nsew", padx=(5, 5), pady=(5, 5))
    return textarea


def create_button(parent, text, command, font=("Arial", 20, 'bold'),
                  width=190, fg_color=None, border_spacing=5):
    button = ctk.CTkButton(parent, text=text, command=command, font=font,
                           width=width, fg_color=fg_color, border_spacing=border_spacing)
    return button


def create_frame(parent, row, column, fg_color='transparent'):
    frame = ctk.CTkFrame(parent, fg_color=fg_color)
    frame.grid(row=row, column=column, sticky="nsew")
    return frame


def configure_tab(tab):
    tab.grid_columnconfigure(0, weight=35, minsize=520)
    tab.grid_columnconfigure(1, weight=30, minsize=200)
    tab.grid_columnconfigure(2, weight=35, minsize=520)


def setup_io_column_from_tab(parent_tab, title_text, button_text, button_command, column):
    column_title = create_label(parent_tab, title_text)
    column_title.grid(row=0, column=column, sticky="nsew", padx=(5, 5), pady=(5, 5))

    column_textbox = create_textarea(parent_tab, row=1, column=column)

    column_error = create_label(parent_tab, '', text_color='red')
    column_error.grid(row=3, column=column, sticky="nsew", padx=(5, 5), pady=(5, 5))

    column_button = create_button(parent_tab, button_text, command=lambda: button_command(column_textbox, column_error))
    column_button.grid(row=2, column=column, sticky="nsew", padx=(5, 5), pady=(5, 5))

    return column_textbox, column_error


def setup_options_column(parent_tab, key_variable, process_func, clear_func, input_textbox, output_textbox,
                         input_error_label, output_error_label, load_menu_func, crypt_func, operation_name="Process"):

    options_column = create_frame(parent_tab, row=1, column=1)
    create_label(options_column, "Enter your key", text_color="black",
                 font=("Arial", 16, 'bold')).pack(pady=(150, 5), fill='x')
    ctk.CTkEntry(options_column, fg_color="#c4c4c4", width=190, font=("Arial", 16),
                 text_color='black', textvariable=key_variable).pack(pady=(0, 10))
    create_button(options_column, f"{operation_name} your message",
                  command=lambda: process_func(input_textbox, output_textbox, key_variable.get(),
                                               input_error_label, crypt_func),
                  border_spacing=10, font=("Arial", 16, 'bold')).pack(pady=(10, 10))
    create_button(options_column, "Clear input",
                  command=lambda: clear_func(input_textbox, output_textbox, key_variable,
                                             input_error_label, output_error_label),
                  border_spacing=10, font=("Arial", 16, 'bold'), fg_color='green').pack(pady=(10, 10))
    create_button(options_column, "Back to main menu",
                  command=lambda: {clear_func(input_textbox, output_textbox, key_variable,
                                              input_error_label, output_error_label),
                                   load_menu_func('MainMenu')},
                  border_spacing=10, font=("Arial", 16, 'bold'), fg_color='red').pack(pady=(10, 10))


def setup_options_column_two_keys(parent_tab, int_key_variable, string_key_variable, process_func, clear_func,
                                  input_textbox, output_textbox, input_error_label, output_error_label, load_menu_func,
                                  crypt_func, operation_name="Process"):

    options_column = create_frame(parent_tab, row=1, column=1)
    create_label(options_column, "Enter integer key", text_color="black",
                 font=("Arial", 16, 'bold')).pack(pady=(150, 5), fill='x')
    ctk.CTkEntry(options_column, fg_color="#c4c4c4", width=190, font=("Arial", 16),
                 text_color='black', textvariable=int_key_variable).pack(pady=(0, 10))
    create_label(options_column, "Enter string key", text_color="black",
                 font=("Arial", 16, 'bold')).pack(pady=(0, 5), fill='x')
    ctk.CTkEntry(options_column, fg_color="#c4c4c4", width=190, font=("Arial", 16),
                 text_color='black', textvariable=string_key_variable).pack(pady=(0, 10))
    create_button(options_column, f"{operation_name} your message",
                  command=lambda: process_func(input_textbox, output_textbox, int_key_variable.get(),
                                               string_key_variable.get(), input_error_label, crypt_func),
                  border_spacing=10, font=("Arial", 16, 'bold')).pack(pady=(10, 10))
    create_button(options_column, "Clear input",
                  command=lambda: clear_func(input_textbox, output_textbox, int_key_variable, string_key_variable,
                                             input_error_label, output_error_label),
                  border_spacing=10, font=("Arial", 16, 'bold'), fg_color='green').pack(pady=(10, 10))
    create_button(options_column, "Back to main menu",
                  command=lambda: {clear_func(input_textbox, output_textbox, int_key_variable, string_key_variable,
                                              input_error_label, output_error_label),
                                   load_menu_func('MainMenu')},
                  border_spacing=10, font=("Arial", 16, 'bold'), fg_color='red').pack(pady=(10, 10))
