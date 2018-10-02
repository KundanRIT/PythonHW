__author__ = 'DS & KK'

"""
CSCI-603: Homework 2 (Forest)
Author: Deepam Shah & Kundan Kumar
"""

from turtle import *
import random
import math

# global constants for window dimensions

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000


def Trunk(height, art):
    """
    Draw the Tree Trunk.
    :param art: turtle
    :param height height of tree trunk
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,height), heading (east), up
    :return: None
    """
    art.down()
    art.left(90)
    art.forward(height)
    art.right(90)
    art.up()


def Triangle(height, art):
    """
    Draw the Triangle.
    :param art: turtle
    :param height side of triangle
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    art.down()
    art.forward(height / 2)
    for j in range(0, 3):
        art.left(120)
        art.forward(height)
    art.backward(height / 2)
    art.up()


def drawTree(tree, art):
    """
    :param art: turtle
    :param tree: list storing type of tree and its trunk height
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: Complete height of tree, Wood in the tree
    """
    height = tree[1]
    Trunk(height, art)
    art.down()
    if tree[0] == 1:
        # drawing pine tree
        Triangle(height / 2, art)
        art.left(180)
        treeHeight = height + (math.sqrt(3) / 2) * (height / 2)
        woodUsed = (5 / 2) * height
    elif tree[0] == 2:
        # drawing maple tree
        art.circle(height / 2)
        art.left(180)
        treeHeight = 2 * height
        woodUsed = height + 2 * math.pi * (height / 2)
    else:
        # drawing mango tree
        art.circle(height / 2)
        art.up()
        art.left(90)
        art.forward(height)
        art.down()
        art.right(90)
        Triangle(height / 4, art)
        art.up()
        art.right(90)
        art.forward(height)
        art.right(90)
        treeHeight = height + height + (math.sqrt(3) / 2) * (height / 4)
        woodUsed = height + height + 2 * math.pi * (height / 2) + \
                   ((3 / 4) * height)
    Trunk(height, art)
    art.right(180)
    return treeHeight, woodUsed


def drawHouse(length, art):
    """
    Draw the House.
    :param art: turtle
    :param length side of the wall of house
    :pre: (relative) pos (0,0), heading (east), down
    :post: (relative) pos (length,0), heading (east), up
    :return: wood used in the house
    """
    art.up()
    art.left(90)
    art.forward(length)
    art.right(180)
    art.down()
    for i in range(0, 3):
        art.forward(length)
        art.left(90)
    art.right(45)
    for i in range(0, 2):
        art.forward(length / 1.41)
        art.left(90)
    art.right(45)
    art.up()
    art.forward(length)
    art.left(90)
    art.forward(length)
    return 2 * length + math.sqrt(2) * length


def drawStar(height, art):
    """
    Draw the Star.
    :param art: turtle
    :param height at which star is drawn
    :pre: (relative) pos (0,0), heading (east), down
    :post: (relative) pos (0,0), heading (east), up
    :return: none
    """
    art.up()
    art.left(90)
    art.forward(height + 10 + 20)
    art.down()
    for i in range(8):
        art.forward(20)
        art.backward(20)
        art.left(45)
    art.up()
    art.backward(height + 10 + 20)
    art.right(90)


def drawSun(dayHouseWall, art):
    """
    Draw the Sun.
    :param art: turtle
    :param dayHouseWall side of the wall of house
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: none
    """
    art.left(90)
    art.forward(3 * dayHouseWall / 2 + 10)
    art.down()
    art.right(90)
    art.circle(25)
    art.up()
    art.right(90)
    art.forward(3 * dayHouseWall / 2 + 10)
    art.left(90)


def main():
    """"
    Main Method
    """
    art = Turtle()
    setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                            WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    art.up()
    art.setx(-400)
    art.sety(-400)
    art.down()
    number = int(input("How many trees in your forest?"))
    trees = {}  # key -> index of tree | value -> [type of tree, height of tree]
    maxheight = height = 0
    starPosition = 0
    requestedHouse = False
    housePosition = None
    for index in range(number):
        typeOfTree = random.randint(1, 3)
        if typeOfTree == 1:  # pine tree
            height = random.randint(50, 200)
            trees[index] = [1, height]
        elif typeOfTree == 2:  # maple tree
            height = random.randint(50, 150)
            trees[index] = [2, height]
        elif typeOfTree == 3:  # mango tree
            height = random.randint(50, 170)
            trees[index] = [3, height]
        if maxheight < height:
            maxheight = height
            starPosition = index
    answer = str(input("Is there a house in the forest?"))
    if "y" in answer.lower():
        requestedHouse = True
        if number > 1:
            housePosition = random.randint(1, number - 1) - 1
        else:
            housePosition = 0
    availableWoods = 0
    if number == 0 and "y":
        if requestedHouse:
            availableWoods = drawHouse(100, art)
        drawStar(100 * 3 / 2, art)
    for index, tree in trees.items():
        treeHeight, woodUsed = drawTree(tree, art)
        availableWoods += woodUsed
        if index == starPosition:
            drawStar(treeHeight, art)
        if index < number - 1 or ((number is 1) and requestedHouse):
            art.down()
            art.forward(100)
        if index == housePosition and requestedHouse:
            availableWoods += drawHouse(100, art)
            if number > 1:
                art.down()
                art.forward(100)
    input("Night is done. Do you want to chop down all trees... Press Enter "
          "for Day")
    print('We have %d units of lumber for the building' % availableWoods)
    dayHouseWall = availableWoods / (2 + math.sqrt(2))
    print('We will build a house with walls %d tall' % dayHouseWall)
    art.clear()
    art.up()
    art.setx(-400)
    art.sety(-400)
    art.down()
    drawHouse(dayHouseWall, art)
    art.up()
    art.forward(100)
    drawSun(dayHouseWall, art)
    mainloop()


if __name__ == '__main__':
    main()
