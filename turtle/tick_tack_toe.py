from turtle import *
import random


def start_screen():
    speed("fastest")
    pensize(5)
    seth(90)
    penup()
    fd(200)
    write("난이도 선택", True, align="center", font=('이서윤체', 40, 'normal'))
    goto(-100, -100)
    pendown()
    fd(100)
    left(90)
    fd(150)
    left(90)
    fd(100)
    left(90)
    fd(75)
    penup()
    left(90)
    fd(40)
    write("쉬움", True, align="center", font=('이서윤체', 20, 'normal'))
    goto(-175, -100)
    pendown()
    goto(-100, -100)
    penup()
    goto(100, -100)
    pendown()
    fd(100)
    right(90)
    fd(150)
    right(90)
    fd(100)
    right(90)
    fd(75)
    right(90)
    penup()
    fd(40)
    write("어려움", True, align="center", font=('이서윤체', 20, 'normal'))
    goto(100, -100)
    pendown()
    right(90)
    fd(150)


def select(x, y):
    if x >= -250 and x <= -100 and y >= -100 and y <= 0:
        nanido_easy()
    if x >= 100 and x <= 250 and y >= -100 and y <= 0:
        pass
    else:
        pass
    print(x, y)


start_screen()
onscreenclick(select)


def make():
    reset()
    speed("fastest")
    penup()
    goto(-300, 100)
    pendown()
    pensize(5)
    fd(600)
    penup()
    goto(-300, -100)
    pendown()
    fd(600)
    penup()
    goto(100, -300)
    left(90)
    pendown()
    fd(600)
    penup()
    goto(-100, -300)
    pendown()
    fd(600)


def nanido_easy():
    make()
    numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def show(x, y):
        column = (x+300) // 200
        row = (y+300) // 200
        if 0 <= column < 3 and 0 <= row < 3:
            print((2-row)*3 + column)
            
        print(x, y)
    onscreenclick(show)


done()
