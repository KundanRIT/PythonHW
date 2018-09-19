__author__ = 'DS & KK'

"""
CSCI-603: Homework 2 (Forest)
Author: Deepam Shah & Kundan Kumar
"""

import turtle as turtle
import random
import math


# global constants for window dimensions

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


def Trunk(height):
    turtle.down()
    turtle.left(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.up()

    """
    Draw the Tree Trunk.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,height), heading (east), up
    :return: None
    """
def Triangle(height):
    turtle.down()
    turtle.forward(height / 2)
    for j in range(0, 3):
        turtle.left(120)
        turtle.forward(height)
    turtle.backward(height / 2)
    turtle.up()

    """
    Draw the Triangle.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """

def drawMaple(height):
    Trunk(height)
    turtle.down()
    turtle.circle(height / 2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    return 2*height, height+2*math.pi*(height/2)

    """
    Draw the Maple crown.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (100,0), heading (east), up
    :return: Wood made by the tree
    """

def drawPine(height):
    Trunk(height)
    Triangle(height/2)
    turtle.left(180)
    Trunk(height)
    turtle.right(180)
    return height+(math.sqrt(3)/2)*(height/2), (5/2)*height

    """
    Draw the Pine Crown
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (100,0), heading (east), up
    :return: Wood made by the tree
    """

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

    """
    Draw the Mango crown.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (100,0), heading (east), up
    :return: Wood made by the tree
    """

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
    return (2*length+math.sqrt(2)*length)

    """
    Draw the House.
    :pre: (relative) pos (0,0), heading (east), down
    :post: (relative) pos (0,0), heading (east), up
    :return: none
    """

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

    """
    Draw the Star.
    :pre: (relative) pos (0,0), heading (east), down
    :post: (relative) pos (0,0), heading (east), up
    :return: none
    """

def drawSun(dayHouseWall):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(3*dayHouseWall/2 + 10)
    turtle.down()
    turtle.right(90)
    turtle.circle(25)
    """
    Draw the Sun.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), down
    :return: none
    """


def drawTree(tree):
    if tree[0] == 1:
        return drawPine(tree[1])
    elif tree[0] == 2:
        return drawMaple(tree[1])
    else:
        return drawMango(tree[1])

def main():
    turtle.up()
    turtle.setx(-400)
    turtle.sety(-400)
    turtle.down()
    number = int(input("How many trees in your forest?"))
    trees = {} # key -> index of tree | value -> [type of tree, height of tree]
    maxheight = height = 0
    starPosition = 0
    requestedHouse = False
    housePosition = None
    for index in range(number):
        typeOfTree = random.randint(1,3)
        if typeOfTree == 1: # pine tree
            height = random.randint(50, 200)
            trees[index] = [1, height]
        elif typeOfTree == 2: # maple tree
            height = random.randint(50, 150)
            trees[index] = [2, height]
        elif typeOfTree == 3: # mango tree
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
    if number==0 and "y":
        if requestedHouse:
            availableWoods = drawHouse(100)
        drawStar(100*3/2)
    for index,tree in trees.items():
        treeHeight, woodUsed = drawTree(tree)
        availableWoods += woodUsed
        if index == starPosition:
            drawStar(treeHeight)
        if index < number-1 or number is 1:
            turtle.down()
            turtle.forward(100)
        if index == housePosition and requestedHouse:
            availableWoods += drawHouse(100)
            if number > 1:
                turtle.down()
                turtle.forward(100)
    input("Night is done. Do you want to chop down all trees... Press Enter "
          "for Day")
    print('We have %d units of lumber for the building' %availableWoods)
    dayHouseWall = availableWoods/(2 + math.sqrt(2))
    print('We will build a house with walls %d tall' %dayHouseWall)
    turtle.clear()
    turtle.up()
    turtle.setx(-400)
    turtle.sety(-400)
    turtle.down()
    drawHouse(dayHouseWall)
    drawSun(dayHouseWall)
    turtle.getscreen()._root.mainloop()

if __name__ == '__main__':
    main()
