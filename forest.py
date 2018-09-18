__author__ = 'DS & KK'

"""
CSCI-603: Homework 2 (Forest)
Author: Deepam Shah & Kundan Kumar
"""

import turtle
import random
import math

"""pop = turtle.Screen()               # creates a graphics window"""

# global constants for window dimensions

WINDOW_WIDTH = 5000
WINDOW_HEIGHT = 5000

"""t.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
"""


def drawTree(number):
    height1 = 0
    for x in range(number):
        height = random.randint(50, 250)
        if height > height1:
            height1 == height

        if height <= 250:
            drawMango(height)
        elif height <= 200:
            drawMaple(height)
        else:
            drawPine(height)
    return height1



def Trunk(height):
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)


def Triangle(height):
    turtle.forward(height / 4)
    for j in range(0, 3):
        turtle.left(120)
        turtle.forward(height / 2)
    turtle.backward(height / 4)


def drawMaple(height):
    Trunk(height)
    turtle.circle(height / 2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    turtle.up()
    turtle.forward(100)
    turtle.down()


def drawPine(height):
    Trunk(height)
    Triangle(height)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    turtle.up()
    turtle.forward(100)
    turtle.down()


def drawMango(height):
    Trunk(height)
    turtle.circle(height / 2)
    turtle.up()
    turtle.left(90)
    turtle.forward(height)
    turtle.down()
    turtle.right(90)
    Triangle(height / 2)
    turtle.up()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(2 * height)
    turtle.left(90)
    turtle.down()


def drawHouse(length):
    turtle.up()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(180)
    turtle.down()
    for i in range(0, 3):
        turtle.forward(length)
        turtle.left(90)
    turtle.right(45)
    for i in range(0, 2):
        turtle.forward(length / 1.41)
        turtle.left(90)
    turtle.right(45)
    turtle.up()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length + 100)


def drawStar(height1):
    turtle.left(90)
    turtle.up()
    turtle.forward(height1+10)
    turtle.down()
    for i in range(8):
        turtle.forward(25)
        turtle.backward(25)
        turtle.left(45)


def drawSun():
    turtle.left(90)
    turtle.forward(300)
    turtle.down()
    turtle.right(90)
    turtle.circle(50)

def main():
    number = int(input("How many trees in your forest?"))
    answer = str(input("Is there a house in the forest?"))
    house = 'y' or 'Y'
    turtle.up()
    turtle.setx(-225)
    turtle.sety(-225)
    turtle.down()

    drawTree(number)
    if answer == house:
        length=random.randint(100, 200)
        drawHouse(length)
    else:
        exit()
    drawStar(380)
    enter = str(input("Night is done... Press Enter for Day"))
    right = ''
    if enter == right:
        print('We have %d units of lumber for the building')
        print('We will build a house with walls %d tall')
        turtle.clear()
        turtle.up()
        turtle.setx(-225)
        turtle.sety(-225)
        turtle.right(90)
        turtle.down()
        drawHouse(250)
        drawSun()
    else:
        exit()
    turtle.getscreen()._root.mainloop()


if __name__ == '__main__':
    main()
