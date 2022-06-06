import time
from turtle import *


def draw_circle(x, y, r):
    penup()
    goto(x, y-r)
    seth(0)
    pendown()
    speed("fastest")
    circle(r)
    penup()


def mark_circle(x, y, r):
    penup()
    goto(x, y-r)
    seth(0)
    pendown()
    speed("fast")
    circle(r)
    penup()


color("white", "green")
begin_fill()
draw_circle(0, 200, 110)
end_fill()
goto(0, 0)
color("white", "blue")
begin_fill()
draw_circle(0, -200, 110)
end_fill()
goto(0, 0)
color("white", "red")
begin_fill()
draw_circle(200, 0, 110)
end_fill()
goto(0, 0)
color("white", "yellow")
begin_fill()
draw_circle(-200, 0, 110)
end_fill()


def play(message):
    def check(my_ans):
        def call(x, y):
            import random
            a = random.randint(1, 4)
            print(x, y)
            print(message)
            play(message + str(a))
            if a == 1:
                color("white", "lightgreen")
                begin_fill()
                mark_circle(0, 200, 110)
                end_fill()
                time.sleep(0.75)
                undo()
            elif a == 2:
                color("white", "lightyellow")
                begin_fill()
                mark_circle(-200, 0, 110)
                end_fill()
                time.sleep(0.75)
                undo()
            elif a == 3:
                color("white", "lightblue")
                begin_fill()
                mark_circle(0, -200, 110)
                end_fill()
                time.sleep(0.75)
                undo()
            else:
                color("white", "lightcoral")
                begin_fill()
                mark_circle(200, 0, 110)
                end_fill()
                time.sleep(0.75)
                undo()
            if (0-x)**2 + (200-y)**2 <= 110**2:
                check(my_ans + "1")

        onscreenclick(call)
    check("")


play("")
done()
