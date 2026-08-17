import colorgram
import turtle as t
import random

#takes images to collect the data of colour with image file specifically named "image.jpg"
#uses colorgram module(addon) use "pip install colorgram.py" to install module {this module takes a processing time of 0.6 s per picture of size 512x512}

colours = colorgram.extract('image.jpg', 10)
t.colormode(255)
rgb = []
for c in colours:
    r_rgb= c.rgb.r
    g_rgb= c.rgb.g
    b_rgb= c.rgb.b
    rgbtupple = (r_rgb, g_rgb, b_rgb)
    rgb.append(rgbtupple)

def coloured_line():
    for i in range(15):
        t.color(random.choice(rgb))
        t.dot(20)
        t.forward(30)

def line_up():
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(450)
    t.left(180)

def main():
    t.penup()
    t.right(180)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    for i in range(15):
        coloured_line()
        line_up()




main()
screen = t.Screen()
screen.exitonclick()
