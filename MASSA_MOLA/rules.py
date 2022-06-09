import turtle
from math import cos, pi
import time
import image
import os
from PIL import Image


def O_h_s(t):
    move = 100 * cos(t)
    return move

def create_image_turtle (name_picture='turtle', formato='gif', width=1, height=1 ):
    '''

    :param name_picture: receives the name of the photo or image inside the image folder
    :return:

    '''
    picture_im = Image.open(f'image/{name_picture}.{formato}')
    picture_out = picture_im.resize((700 * width, 700 * height))
    picture_out.save(f'image\\{name_picture}save.gif', 'GIF')
    image = turtle.Turtle()
    screen_add = turtle.Screen()
    screen_add.addshape(f'image/{name_picture}save.gif')
    image.shape(f'image/{name_picture}save.gif')

def creat_turtle(turtle_name, shape = 'square', color = 'black', height = 1, width = 1, size = 1, posx = 0,
                 posy = 0, speed = 6):
    turtle_name = turtle.Turtle()
    turtle_name.hideturtle()
    turtle_name.penup()
    turtle_name.shape(shape)
    turtle_name.color(color)
    turtle_name.shapesize(height, width, size)
    turtle_name.setposition(posx, posy)
    turtle_name.speed(speed)
    return turtle_name.showturtle()






