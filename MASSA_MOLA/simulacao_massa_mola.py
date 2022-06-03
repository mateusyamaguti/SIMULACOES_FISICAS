import time
import turtle
from math import cos
import equations


'''Creat a Turtle'''
mass = turtle.Turtle()
mass.penup()
mass.shape('circle')
mass.speed(1)

'''initial parameters'''
t = 0

'''Oscillation test'''
while True:
    t += 1
    mass.sety(equations.O_h_s(t))


