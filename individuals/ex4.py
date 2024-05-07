# !/usr/bin/env python3
# -*- coding: utf-8 -

#Решите задачу: Создайте на холсте подобное изображение:

import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Анапа 2007")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    center_x = canvas.winfo_reqwidth() / 2
    center_y = canvas.winfo_reqheight() / 2

    # Рисуем дом
    house_width = 100
    house_height = 120
    canvas.create_rectangle(
        center_x - house_width / 2,
        center_y - house_height / 2,
        center_x + house_width / 2,
        center_y + house_height / 2,
        fill="lightblue",
    )

    # Рисуем крышу дома
    canvas.create_polygon(
        center_x,
        center_y - house_height / 2,
        center_x - house_width / 2,
        center_y - house_height / 2,
        center_x,
        center_y - house_height / 2 - 40,
        center_x + house_width / 2,
        center_y - house_height / 2,
        fill="lightblue",
    )

    # Рисуем солнце в правом верхнем углу
    sun_radius = 30
    sun_center_x = 350
    sun_center_y = 50
    canvas.create_oval(
        sun_center_x - sun_radius,
        sun_center_y - sun_radius,
        sun_center_x + sun_radius,
        sun_center_y + sun_radius,
        fill="orange",
    )

    # Рисуем траву в нижней части холста
    grass_color = "green"
    grass_height = 20
    line_width = 3
    for i in range(0, canvas.winfo_reqwidth(), 20):
        x = i
        y_start = canvas.winfo_reqheight()
        y_end = y_start - grass_height
        x_end = x + grass_height / 2  # Добавляем уклон вправо к верху
        canvas.create_line(
            x, y_start, x_end, y_end, fill=grass_color, width=line_width
        )

    root.mainloop()
