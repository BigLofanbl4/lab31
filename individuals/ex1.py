# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def add_to_cart():
    selected_items = list_box_products.curselection()
    for i in reversed(selected_items):
        cart_list.insert(tk.END, list_box_products.get(i))
        list_box_products.delete(i)


def remove_from_cart():
    selected_items = cart_list.curselection()
    for i in reversed(selected_items):
        list_box_products.insert(tk.END, cart_list.get(i))
        cart_list.delete(i)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Список покупок")

    list_box_products = tk.Listbox(
        root, selectmode="extended", height=10, exportselection=0
    )
    list_box_products.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0), pady=10)

    products = [
        "Хлеб",
        "Молоко",
        "Яйца",
        "Колбаса",
        "Сыр",
        "Чай",
        "Сахар",
        "Соль",
    ]
    for product in products:
        list_box_products.insert(tk.END, product)

    cart_list = tk.Listbox(
        root, selectmode="extended", height=10, exportselection=0
    )
    cart_list.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)

    add_button = tk.Button(
        root, text="Добавить в корзину ->", command=add_to_cart
    )
    add_button.pack(pady=5, padx=10)
    remove_button = tk.Button(
        root, text="<- Удалить из корзины", command=remove_from_cart
    )
    remove_button.pack(pady=5, padx=10)

    root.mainloop()
