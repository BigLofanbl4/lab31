# !/usr/bin/env python3
# -*- coding: utf-8 -

#Решите задачу: напишите программу по следующему описанию. Нажатие Enter в
#однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
#Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна
#копироваться в текстовое поле.

import tkinter as tk


def move_to_list(event):
    text = entry.get()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)


def copy_to_entry(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_text = listbox.get(selected_indices[0])
        entry.delete(0, tk.END)
        entry.insert(0, selected_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Entry to Listbox")

    entry = tk.Entry(root)
    entry.bind("<Return>", move_to_list)
    entry.pack(pady=10)

    listbox = tk.Listbox(root)
    listbox.bind("<Double-Button-1>", copy_to_entry)
    listbox.pack(pady=10)

    root.mainloop()
