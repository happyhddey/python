import time
import random

from turtle import *


def draw_circle(x, y, r):
    penup()
    goto(x, y - r)
    seth(0)
    pendown()
    speed("fastest")
    circle(r)
    penup()


def mark_circle(x, y, r):
    penup()
    goto(x, y - r)
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

answer = []


def play():
    a = random.randint(1, 4)
    answer.append(a)
    # answer를 보여주기
    print(answer)

    my_ans = []

    def check():
        def call(x, y):
            print(x, y)

            if (0 - x) ** 2 + (200 - y) ** 2 <= 110 ** 2:
                my_ans.append(1)
            elif (-200 - x) ** 2 + (0 - y) ** 2 <= 110 ** 2:
                my_ans.append(2)
            elif (0 - x) ** 2 + (-200 - y) ** 2 <= 110 ** 2:
                my_ans.append(3)
            elif (200 - x) ** 2 + (0 - y) ** 2 <= 110 ** 2:
                my_ans.append(4)

            b = len(my_ans)-1
            if len(answer) != len(my_ans):
                if answer[b] == my_ans[b]:
                    check()
                else:
                    reset()
                    penup()
                    write("틀렸습니다", align="left", font=('Arial', 100, 'normal'))
            elif answer[b] == my_ans[b]:
                play()
            else:
                onscreenclick(None)
                reset()
                penup()
                write("틀렸습니다", True, align="center", font=('Arial', 100, 'normal'))

        onscreenclick(call)
    check()


play()
done()
