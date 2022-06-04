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
mass.color('red')
mass.shapesize(1, 1, 1)
mass.speed(1)

suport = turtle.Turtle()
suport.hideturtle()
suport.penup()
suport.shape('square')
suport.color('violet')
suport.shapesize(1, 3, 20)
mass.speed(1)

'''initial parameters'''
t = 0
suport.setposition(-200, 120)
suport.showturtle()

mass.setposition(-200, 0)
mass.showturtle()


'''Oscillation test'''

while True:
    t += 1
    mass.sety(rules.O_h_s(t))
