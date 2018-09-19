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

def Trunk(height):
    turtle.down()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.up()

def Triangle(height):
    turtle.down()
    turtle.forward(height / 2)
    for j in range(0, 3):
        turtle.left(120)
        turtle.forward(height)
    turtle.backward(height / 2)
    turtle.up()

def drawMaple(height):
    Trunk(height)
    turtle.down()
    turtle.circle(height / 2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    return 2*height, height+2*math.pi*(height/2)

def drawPine(height):
    Trunk(height)
    Triangle(height/2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    return height+(math.sqrt(3)/2)*(height/2), (5/2)*height

def drawMango(height):
    Trunk(height)
    turtle.down()
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
    turtle.forward(length)

def drawStar(height):
    turtle.up()
    turtle.left(90)
    turtle.forward(height + 10 + 20)
    turtle.down()
    for i in range(8):
        turtle.forward(20)
        turtle.backward(20)
        turtle.left(45)
    turtle.up()
    turtle.backward(height + 10 + 20)
    turtle.right(90)

def drawSun(woodUsed):
    turtle.left(90)
    turtle.forward(woodUsed/4 +10)
    turtle.down()
    turtle.right(90)
    turtle.circle(50)

def drawTree(tree):
    if tree[0] == 1:
        return drawPine(tree[1])
    elif tree[0] == 2:
        return drawMaple(tree[1])
    else:
        return drawMango(tree[1])

def main():
    turtle.up()
    turtle.setx(-225)
    turtle.sety(-225)
    turtle.down()
    number = int(input("How many trees in your forest?"))
    trees = {}
    maxheight = height = 0
    starPosition = 0
    requestedHouse = False
    housePosition = None
    for index in range(number):
        typeOfTree = random.randint(1,3)
        if typeOfTree == 1:
            height = random.randint(50, 200)
            trees[index] = [1, height]
        elif typeOfTree == 2:
            height = random.randint(50, 150)
            trees[index] = [2, height]
        elif typeOfTree == 3:
            height = random.randint(50, 170)
            trees[index] = [3, height]
        if maxheight < height:
            maxheight = height
            starPosition = index
    answer = str(input("Is there a house in the forest?"))
    if "y" in answer.lower():
        requestedHouse = True
        if number > 1:
            housePosition = random.randint(1, number-1) - 1
        else:
            housePosition = 0
    availableWoods = 0
    for index,tree in trees.items():
        treeHeight, woodUsed = drawTree(tree)
        availableWoods += woodUsed
        if index == starPosition:
            drawStar(treeHeight)
        turtle.down()
        turtle.forward(100)
        if index == housePosition and requestedHouse:
            drawHouse(100)
            availableWoods += (2*100+2*math.sqrt(2)*100)
            turtle.down()
            turtle.forward(100)
    enter = str(input("Night is done... Press Enter for Day"))
    right = ''
    if enter == right:
        print('We have %d units of lumber for the building' %woodUsed)
        print('We will build a house with walls %d tall' %(woodUsed/(2 + math.sqrt(2))))
        turtle.clear()
        turtle.up()
        turtle.setx(-225)
        turtle.sety(-225)
        turtle.down()
        drawHouse(250)
        drawSun(woodUsed)
    else:
        exit()
    turtle.getscreen()._root.mainloop()

if __name__ == '__main__':
    main()