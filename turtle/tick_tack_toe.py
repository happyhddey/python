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

print("hello")

def nanido_easy():
    make()
    numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def show(x, y):
        if x >= -300 and x <= -100 and y >= 100 and y <= 300:
            if 1 in numbs:
                print(1)
                numbs.remove(1)
                
            else:
                pass
        elif x >= -100 and x <= 100 and y >= 100 and y <= 300:
            if 2 in numbs:
                print(2)
                numbs.remove(2)
            else:
                pass
        elif x >= 100 and x <= 300 and y >= 100 and y <= 300:
            if 3 in numbs:
                print(3)
                numbs.remove(3)
            else:
                pass
        elif x >= -300 and x <= -100 and y >= -100 and y <= 100:
            if 4 in numbs:
                print(4)
                numbs.remove(4)
            else:
                pass
        elif x >= -100 and x <= 100 and y >= -100 and y <= 100:
            if 5 in numbs:
                print(5)
                numbs.remove(5)
            else:
                pass
        elif x >= 100 and x <= 300 and y >= -100 and y <= 100:
            if 6 in numbs:
                print(6)
                numbs.remove(6)
            else:
                pass
        elif x >= -300 and x <= -100 and y >= -300 and y <= -100:
            if 7 in numbs:
                print(7)
                numbs.remove(7)
            else:
                pass
        elif x >= -100 and x <= 100 and y >= -300 and y <= -100:
            if 8 in numbs:
                print(8)
                numbs.remove(8)
            else:
                pass
        elif x >= 100 and x <= 300 and y >= -300 and y <= -100:
            if 9 in numbs:
                print(9)
                numbs.remove(9)
            else:
                pass
        else:
            pass
        print(x, y)
    onscreenclick(show)


done()
