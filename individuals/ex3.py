# !/usr/bin/env python3
# -*- coding: utf-8 -

#Решите задачу: напишите программу по описанию. Размеры многострочного текстового поля
#определяются значениями, введенными в однострочные текстовые поля. Изменение
#размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши Enter.

import tkinter as tk


def resize_text_field():
    try:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        text_field.config(width=new_width, height=new_height)
    except ValueError:
        print("Пожалуйста, введите числовые значения для ширины и высоты.")


def on_focus_in(event):
    text_field.config(bg="white")


def on_focus_out(event):
    text_field.config(bg="lightgrey")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ресайзер текстового поля")

    width_entry = tk.Entry(root)
    width_entry.pack(pady=(10, 0))
    height_entry = tk.Entry(root)
    height_entry.pack(pady=10)

    resize_button = tk.Button(
        root, text="Изменить размер", command=resize_text_field
    )
    resize_button.pack(pady=10)

    root.bind("<Return>", lambda event: resize_text_field())

    text_field = tk.Text(root, width=20, height=5, bg="lightgrey")
    text_field.pack(pady=10)
    text_field.bind("<FocusIn>", on_focus_in)
    text_field.bind("<FocusOut>", on_focus_out)

    root.mainloop()
