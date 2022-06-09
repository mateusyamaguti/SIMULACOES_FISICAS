import time
import turtle
from math import cos
import rules

title = turtle.title("Simulation mass - spring")

'''Create scenery'''
laboratoty = rules.create_image_turtle('laboratorio','gif', 2, 1)


'''Create a Turtle'''
mass = turtle.Turtle()
mass.hideturtle()
mass.penup()
mass.shape('circle')
mass.color('black')
mass.shapesize(1, 1, 1)
mass.speed(1)

suport = turtle.Turtle()
suport.hideturtle()
suport.penup()
suport.shape('square')
suport.color('violet')
suport.shapesize(1, 3, 20)
mass.speed(1)

button_start = turtle.Turtle()
button_start.hideturtle()
button_start.penup()
button_start.shape('square')
button_start.color('green')
button_start.shapesize(1, 2, 10)
mass.speed(1)

button_pause = turtle.Turtle()
button_pause.hideturtle()
button_pause.penup()
button_pause.shape('square')
button_pause.color('red')
button_pause.shapesize(1, 2, 10)

mass.speed(1)

'''initial parameters'''
t = 0
suport.setposition(-200, 120)
suport.showturtle()

button_start.setposition(-120, 140)
button_start.showturtle()

button_pause.setposition(-120, 100)
button_pause.showturtle()

mass.setposition(-200, 0)
mass.showturtle()


'''Oscillation test'''


def pause(x, y):
    button_pause.right(0)
    button_pause.forward(0)
    while True:
        mass.sety(0)


def start(x, y):
    button_start.right(0)
    button_start.forward(0)
    t = 0
    while t >= 0:
        t += 1
        mass.sety(rules.O_h_s(t))



button_start.onclick(start)
button_pause.onclick(pause)



turtle.mainloop()