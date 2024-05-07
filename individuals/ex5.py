# !/usr/bin/env python3
# -*- coding: utf-8 -

#Решите задачу: в данной программе создается анимация круга, который движется от левой
#границы холста до правой:
#from tkinter import *
#def motion():
#   c.move(ball, 1, 0)
#   if c.coords(ball)[2] < 300:
#       root.after(10, motion)
#root = Tk()
#c = Canvas(root, width=300, height=200,
#          bg="white")
#c.pack()
#ball = c.create_oval(0, 100, 40, 140,
#                    fill='green')
#motion()
#root.mainloop()
#Выражение c.coords(ball) возвращает список текущих координат объекта (в данном
#случае это ball). Третий элемент списка соответствует его второй координате x.
#Метод after вызывает функцию, переданную вторым аргументом, через количество
#миллисекунд, указанных первым аргументом.

from tkinter import *


def motion(event):
    current_coords = c.coords(ball)
    center_x = (current_coords[0] + current_coords[2]) / 2
    center_y = (current_coords[1] + current_coords[3]) / 2

    delta_x = (event.x - center_x) / 50
    delta_y = (event.y - center_y) / 50

    move_ball(delta_x, delta_y, event.x, event.y)


def move_ball(delta_x, delta_y, target_x, target_y):
    c.move(ball, delta_x, delta_y)

    current_coords = c.coords(ball)
    center_x = (current_coords[0] + current_coords[2]) / 2
    center_y = (current_coords[1] + current_coords[3]) / 2

    # Проверяем, достиг ли круг конечной точки
    if abs(center_x - target_x) > abs(delta_x) or abs(
        center_y - target_y
    ) > abs(delta_y):
        # Если не достиг, продолжаем движение
        root.after(10, lambda: move_ball(delta_x, delta_y, target_x, target_y))


if __name__ == "__main__":
    root = Tk()
    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()
    ball = c.create_oval(0, 100, 40, 140, fill="green")

    c.bind("<Button-1>", motion)

    root.mainloop()
