from turtle import *
from math import *

'''
Main Method
- Starts a Turtle
- Sets Initial Position
- Draws the Name "KUNDAN KUMAR"
'''
def main():
    myTurtle = Turtle()
    myTurtle.penup()
    myTurtle.goto(-400,0)
    drawLetterK(myTurtle)
    drawLetterU(myTurtle)
    drawLetterN(myTurtle)
    drawLetterD(myTurtle)
    drawLetterA(myTurtle)
    drawLetterN(myTurtle)
    giveSpace(myTurtle)
    drawLetterK(myTurtle)
    drawLetterU(myTurtle)
    drawLetterM(myTurtle)
    drawLetterA(myTurtle)
    drawLetterR(myTurtle)
    mainloop()

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterA(myTurtle):
    # draws letter A
    aAngle = degrees(atan(2))
    myTurtle.pendown()
    myTurtle.left(aAngle)
    myTurtle.forward(25*sqrt(5))
    myTurtle.right(2*aAngle)
    myTurtle.forward(25*sqrt(5))
    myTurtle.backward(25*sqrt(5)/2)
    myTurtle.right(180-aAngle)
    myTurtle.forward(25)
    myTurtle.penup()
    myTurtle.left(60)
    myTurtle.forward(25*sqrt(5)/2)
    myTurtle.left(120)
    myTurtle.forward(50)
    giveSpace(myTurtle)

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterD(myTurtle):
    # draws letter D
    myTurtle.pendown()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(25)
    myTurtle.backward(25)
    myTurtle.right(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(25)
    myTurtle.circle(25, 180)
    myTurtle.left(90)
    myTurtle.penup()
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(25)
    giveSpace(myTurtle)
    
'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterK(myTurtle):
    # draws letter K
    kAngle = degrees(atan(2))
    myTurtle.pendown()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.backward(25)
    myTurtle.right(kAngle)
    myTurtle.forward(25*sqrt(5))
    myTurtle.backward(25*sqrt(5))
    myTurtle.right(180-2*kAngle)
    myTurtle.forward(25*sqrt(5))
    myTurtle.backward(25*sqrt(5))
    myTurtle.right(kAngle)
    myTurtle.forward(25)
    myTurtle.left(90)
    myTurtle.penup()
    myTurtle.forward(50)
    giveSpace(myTurtle)

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterM(myTurtle):
    # draws letter M
    mAngle = degrees(atan(1/2))
    myTurtle.pendown()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(180-mAngle)
    myTurtle.forward(25*sqrt(5))
    myTurtle.left(180-2*mAngle)
    myTurtle.forward(25*sqrt(5))
    myTurtle.right(180-mAngle)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.penup()
    giveSpace(myTurtle)

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterN(myTurtle):
    # draws letter N
    myTurtle.pendown()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(135)
    myTurtle.forward(50*sqrt(2))
    myTurtle.left(135)
    myTurtle.forward(50)
    myTurtle.backward(50)
    myTurtle.right(90)
    myTurtle.penup()
    giveSpace(myTurtle)

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterR(myTurtle):
    # draws letter R
    rAngle = degrees(atan(5/2))
    myTurtle.pendown()
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.right(90)
    myTurtle.forward(35)
    myTurtle.backward(35)
    myTurtle.right(90)
    myTurtle.forward(30)
    myTurtle.left(90)
    myTurtle.forward(35)
    myTurtle.circle(15, 180)
    myTurtle.forward(35)
    myTurtle.left(90)
    myTurtle.forward(30)
    myTurtle.left(rAngle)
    myTurtle.forward(10*sqrt(29))
    myTurtle.penup()
    myTurtle.left(90-rAngle)
    giveSpace(myTurtle)

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(70,0) heading(east) up
 :return None
'''
def drawLetterU(myTurtle):
    # draws letter U
    myTurtle.left(90)
    myTurtle.forward(25)
    myTurtle.pendown()
    myTurtle.forward(25)
    myTurtle.backward(25)
    myTurtle.right(90)
    myTurtle.penup()
    myTurtle.forward(50)
    myTurtle.pendown()
    myTurtle.left(90)
    myTurtle.forward(25)
    myTurtle.backward(25)
    myTurtle.circle(25,-180)
    myTurtle.right(90)
    myTurtle.penup()
    myTurtle.backward(50)
    myTurtle.left(90)
    myTurtle.forward(25)
    myTurtle.left(90)
    giveSpace(myTurtle)

'''
 :pre (relative) pos(0,0) heading(east) up
 :post (relative) pos(20,0) heading(east) up
 :return None
'''
def giveSpace(myTurtle):
    myTurtle.penup()
    myTurtle.forward(20)

if __name__=="__main__":
    main()