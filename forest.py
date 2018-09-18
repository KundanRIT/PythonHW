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
    maxheight = 0
    maxHeightPosition = 0
    woods = 0
    maxTreeHeight = 0
    for x in range(number):
        treeType = random.randint(1,3)
        if treeType == 1:
            height = random.randint(50, 200)
            treeheight, woodUsed = drawPine(height)
        elif treeType == 2:
            height = random.randint(50, 150)
            treeheight, woodUsed = drawMaple(height)
        else:
            height = random.randint(50, 250)
            treeheight, woodUsed = drawMango(height)
        woods += woodUsed
        if maxheight < height:
            maxheight = height
            maxHeightPosition = x
            maxTreeHeight = treeheight
    return maxTreeHeight, maxHeightPosition, woods

def Trunk(height):
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)


def Triangle(height):
    turtle.forward(height / 2)
    for j in range(0, 3):
        turtle.left(120)
        turtle.forward(height)
    turtle.backward(height / 2)


def drawMaple(height):
    Trunk(height)
    turtle.circle(height / 2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    turtle.forward(100)
    return 2*height, height+2*math.pi*(height/2)


def drawPine(height):
    Trunk(height)
    Triangle(height/2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    turtle.forward(100)
    return height+(math.sqrt(3)/2)*(height/2), (5/2)*height


def drawMango(height):
    Trunk(height)
    turtle.circle(height / 2)
    turtle.up()
    turtle.left(90)
    turtle.forward(height)
    turtle.down()
    turtle.right(90)
    Triangle(height / 4)
    turtle.up()
    turtle.right(90)
    turtle.forward(2 * height)
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    return height+height+(math.sqrt(3)/2)*(height/4), \
           height+height+2*math.pi*(height/2)+((3/4)*(height))


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


def drawStar(maxHeight, maxHeightPosition):
    turtle.up()
    turtle.backward(maxHeightPosition*100)
    turtle.left(90)
    turtle.forward(maxHeight + 10 + 25)
    turtle.down()
    for i in range(8):
        turtle.forward(25)
        turtle.backward(25)
        turtle.left(45)
    turtle.up()
    turtle.backward(maxHeight + 10 + 25)
    turtle.right(90)
    turtle.forward(maxHeightPosition * 100)

def drawSun():
    turtle.left(90)
    turtle.forward(300)
    turtle.down()
    turtle.right(90)
    turtle.circle(50)

def main():
    number = int(input("How many trees in your forest?"))
    answer = str(input("Is there a house in the forest?"))
    turtle.up()
    turtle.setx(-225)
    turtle.sety(-225)
    turtle.down()
    maxheight, maxheightPosition, woodUsed = drawTree(number)
    if "y" in answer.lower():
        drawHouse(100)
        woodUsed += (2*100+2*math.sqrt(2)*100)
    drawStar(maxheight, number - maxheightPosition)
    enter = str(input("Night is done... Press Enter for Day"))
    right = ''
    if enter == right:
        print('We have %d units of lumber for the building' %woodUsed)
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