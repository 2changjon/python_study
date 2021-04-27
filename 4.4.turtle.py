import turtle
import random


def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)


def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)  #
    turtle.shapesize(tSize)  #
    r = random.random()
    g = random.random()
    b = random.random()


pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이 그림')  # 윈도우창의 제목을 설정함
turtle.shape('turtle')  # 거북이 모양을 결정함
turtle.pensize(pSize)  # 그릴 선의 두께를 설정함

turtle.onscreenclick(screenLeftClick, 1)  # 마우스 왼쪽 버튼
turtle.onscreenclick(screenMidClick, 2)  # 마우스 중간 버튼
turtle.onscreenclick(screenRightClick, 3)  # 마우스 오른쪽 버튼

turtle.done()
