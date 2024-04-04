import tkinter as tk
from tkinter import filedialog


def open_from_file(textarea, error_label):
    file = filedialog.askopenfile(initialdir='C:\\Users\\mxmvo\\OneDrive\\Desktop\\TSI_folder',
                                  title='Select a file', filetypes=(('txt files', '*.txt'),))

    if file:
        content = file.read()
        file.close()

        if content.strip():
            textarea.delete("1.0", tk.END)
            textarea.insert(tk.END, content)
            error_label.configure(text='')
        else:
            error_label.configure(text='File content is empty or invalid')
    else:
        error_label.configure(text='Error opening the file')


def save_to_file(textarea, error_label):
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\mxmvo\\OneDrive\\Desktop\\TSI_folder',
                                    title='Save file as', filetypes=(('txt files', '*.txt'),),
                                    defaultextension='.txt')
    if file:
        try:
            content = textarea.get("1.0", "end-1c")
            file.write(content)
            error_label.configure(text='File saved successfully')
        except Exception as e:
            error_label.configure(text='Error saving the file')
        finally:
            file.close()
    else:
        error_label.configure(text='An error occurred. Try again')