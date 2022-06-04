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






