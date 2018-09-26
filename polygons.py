# polygons.py (Python HW 3)
# Author: Kundan Kumar (kk7272) & Deepam Shah (ds3689)
# This program draws a polygons using recursion and prints total distance
# travelled by turtle while drawing all polygons. side# and toFill or notToFill
# is provided by command line arguments. Eg. polygons.py [3-8] [fill|unfill]

from turtle import *
import sys

COLORS = ['red','green','indigo','blue','purple','yellow']
# Uncomment this to use randomly genertaed colors
# COLORS = [
#         (random(),random(),random()),
#         (random(),random(),random()),
#         (random(),random(),random()),
#         (random(),random(),random()),
#         (random(),random(),random()),
#         (random(),random(),random()),
# ]


def drawPolygon(side, length, fill, vector):
    '''
    Creates a polygons of sides side, side-1, side-2 .... 3 recursively
    with each length getting decreased by 2
    :param side: number of sides in the polygon
    :param length: length of side in the polygon
    :param fill: True -> to fill polygons, False otherwise
    :param vector: turtle object
    :pre: relative, pos(0,0), heading east, down
    :post: relative, pos(0,0), heading east, down
    :return:
    '''
    # change color of turtle pen as specified in COLORS
    vector.color(COLORS[side - 3])
    # change pensize depending on the length of side
    vector.pensize(length/25)
    if side == 3:
        # base case (create a polygon of side 3)
        if fill:
            vector.begin_fill()
        for _ in range(side):
            vector.left(360 / side)
            vector.forward(length)
        if fill:
            vector.end_fill()
        return side * length
    else:
        # recursive case
        distance = 0
        if fill:
            # fill the polygon before going for recursion when fill is True
            vector.begin_fill()
            for i in range(side):
                vector.forward(length)
                vector.left(360 / side)
            vector.end_fill()
        for i in range(side):
            # creates a regular polygon of side sides and of size length
            vector.color(COLORS[side - 3])
            vector.pensize(length / 25)
            if fill:
                vector.penup()
            vector.forward(length)
            if fill:
                vector.pendown()
            vector.right((360/(side-1))-(360/side))
            # traditional recursion. Waits for the result of the recursion
            distance += drawPolygon(side - 1, length / 2, fill, vector)
            vector.left((360/(side-1))-(360/side))
            vector.left(360/side)
        # returns accumulated distance travelled by turtle
        return side * length + distance


def main():
    '''
    This is the main method.
    It initializes turtle and calls function drawPolygon which recursively
    draws all polygons
    :return: None
    '''
    sides = 0
    fill = ""
    try:
        sides = int(sys.argv[1])
        if sides > 8 or sides < 3:
            print("SideOutOfBoundError: Sides value should be inclusively "
                  "between 3 and 8")
            exit(1)
    except ValueError: # catch when side is not numeric
        print("SideNotFoundError: Side Value is not entered or is not numeric",
              file=sys.stderr)
        exit(1)
    except IndexError: # catch when side# or fill/unfill value is not entered
        print("SideNotFoundError: Side Value is not entered or is not numeric",
              file=sys.stderr)
        exit(1)
    try:
        fill = str(sys.argv[2]).lower()
        if fill is "fill" or fill is "unfill":
            print("FillOutOfBoundError: Fill value should be either fill "
                  "or unfill", file=sys.stderr)
            exit(1)
    except IndexError: # catch when fill/unfill value is not entered
        print("FillNotFoundError: Fill Value is not entered", file=sys.stderr)
        exit(1)
    toFill = fill == 'fill'
    tracer(False) # removes turtle move animation
    vector = Turtle()
    # increase turtle window size (width= and height=1 => fullscreen)
    vector.window = Screen()
    vector.window.setup(width=.9, height=.9, startx=None, starty=None)
    vector.penup()
    vector.goto(400, 400)
    # write authors name on turtle screen
    vector.write("Kundan Kumar (kk7272)", align="right",
                 font=("Monotype Corsiva", 12, "normal", "italic"))
    vector.goto(400, 380)
    vector.write("Deepam Shah (ds3689)", align="right",
                 font=("Monotype Corsiva", 12, "normal", "italic"))
    vector.goto(-200,-200)
    vector.pendown()
    # distance accumulates the distance travelled by turtle to draw all polygons
    distance = drawPolygon(sides, 200, toFill, vector)
    print("Sum: ", distance)
    update()
    mainloop()


if __name__ == '__main__':
    main()