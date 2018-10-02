import turtle                   # allows us to use the turtles library
pop = turtle.Screen()           # creates a graphics window
deepam = turtle.Turtle()        # making the new turtle object with name deepam
deepam.speed(0)                 # increasing the speed of turtle on the graphics page

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

def drawLetterD():
    deepam.left(90)
    deepam.forward(100)
    deepam.right(90)
    deepam.forward(80)
    deepam.right(45)
    deepam.forward(20*1.41)
    deepam.right(45)
    deepam.forward(60)
    deepam.right(45)
    deepam.forward(20*1.41)
    deepam.right(45)
    deepam.forward(80)
    deepam.up()
    deepam.right(180)
    deepam.forward(120)


def drawLetterE():
    deepam.down()
    deepam.left(90)
    deepam.forward(100)
    deepam.right(90)
    deepam.forward(100)
    deepam.backward(100)
    deepam.right(90)
    deepam.forward(50)
    deepam.left(90)
    deepam.forward(80)
    deepam.backward(80)
    deepam.right(90)
    deepam.forward(50)
    deepam.left(90)
    deepam.forward(100)
    deepam.up()
    deepam.forward(20)

def drawLetterP():
    deepam.down()
    deepam.left(90)
    deepam.forward(100)
    deepam.right(90)
    deepam.forward(90)
    deepam.right(45)
    deepam.forward(10*1.41)
    deepam.right(45)
    deepam.forward(30)
    deepam.right(45)
    deepam.forward(10*1.41)
    deepam.right(45)
    deepam.forward(90)
    deepam.left(90)
    deepam.forward(50)
    deepam.left(90)
    deepam.up()
    deepam.forward(120)

def drawLetterA():
    deepam.down()
    deepam.left(60)
    deepam.forward(111.8)
    deepam.right(120)
    deepam.forward(111.8)
    deepam.backward(55.9)
    deepam.right(120)
    deepam.forward(55.9)
    deepam.backward(55.9)
    deepam.left(120)
    deepam.forward(55.9)
    deepam.left(60)
    deepam.up()
    deepam.forward(20)

def drawLetterM():
    deepam.down()
    deepam.left(90)
    deepam.forward(100)
    deepam.right(135)
    deepam.forward(50*1.41)
    deepam.left(90)
    deepam.forward(50*1.41)
    deepam.right(135)
    deepam.forward(100)
    deepam.up()
    deepam.left(90)
    deepam.forward(20)

def drawLetterS():
    deepam.forward(90)
    deepam.backward(90)
    deepam.right(135)
    deepam.forward(10*1.41)
    deepam.left(45)
    deepam.forward(30)
    deepam.left(45)
    deepam.forward(10*1.41)
    deepam.left(45)
    deepam.forward(80)
    deepam.right(45)
    deepam.forward(10*1.41)
    deepam.right(45)
    deepam.forward(30)
    deepam.right(45)
    deepam.forward(10*1.41)
    deepam.right(45)
    deepam.forward(90)
    deepam.up()
    deepam.backward(120)
    deepam.right(180)

def drawLetterH():
    deepam.down()
    deepam.left(90)
    deepam.forward(100)
    deepam.backward(50)
    deepam.right(90)
    deepam.forward(100)
    deepam.right(90)
    deepam.backward(50)
    deepam.forward(100)
    deepam.left(90)
    deepam.up()
    deepam.forward(20)


def main():

    deepam.up()
    deepam.setx(-300)       #setting the x and y coordinates so that the turtle
    deepam.sety(50)         #The turtle starts at a position 
    deepam.down()
    drawLetterD()
    drawLetterE()
    drawLetterE()
    drawLetterP()
    drawLetterA()
    drawLetterM()
    deepam.up()
    deepam.setx(-300)
    deepam.sety(0)
    deepam.down()
    drawLetterS()
    drawLetterH()
    drawLetterA()
    drawLetterH()
    pop.exitonclick()


if __name__ == '__main__':
    main()
