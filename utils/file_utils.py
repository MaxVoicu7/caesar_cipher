import tkinter as tk
from tkinter import filedialog


def open_from_file(textarea, error_label):
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\mxmvo\\OneDrive\\Desktop\\TSI_folder',
                                          title='Select a file', filetypes=(('txt files', '*.txt'),))

    if filepath:
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            if content.strip():
                textarea.delete("1.0", tk.END)
                textarea.insert(tk.END, content)
                error_label.configure(text='File loaded successfully')
            else:
                error_label.configure(text='File content is empty or invalid')
        except Exception as e:
            error_label.configure(text=f'Error opening the file: {str(e)}')
            print(e)
    else:
        error_label.configure(text='No file selected. Try again.')


def save_to_file(textarea, error_label):
    filepath = filedialog.asksaveasfilename(initialdir='C:\\Users\\mxmvo\\OneDrive\\Desktop\\TSI_folder',
                                            title='Save file as', filetypes=(('txt files', '*.txt'),),
                                            defaultextension='.txt')
    if filepath:
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                content = textarea.get("1.0", "end-1c")
                file.write(content)
            error_label.configure(text='File saved successfully')
        except Exception as e:
            error_label.configure(text=f'Error saving the file: {str(e)}')
            print(e)
    else:
        error_label.configure(text='No file selected. Try again.')
