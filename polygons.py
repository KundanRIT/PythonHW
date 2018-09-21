from turtle import *
from random import *

# COLORS = ['red','green','brown','blue','purple','yellow']
# COLORS = ['yellow','purple','blue','brown','green','red']


def recursion(side, length, fill, COLORS, vector):
    vector.color(COLORS[side - 3])
    if side == 3:
        if fill:
            vector.begin_fill()
        for _ in range(side):
            # vector.forward(length)
            vector.left(360 / side)
            vector.forward(length)
        if fill:
            vector.end_fill()
    else:
        if fill:
            vector.begin_fill()
            for i in range(side):
                vector.forward(length)
                vector.left(360 / side)
            vector.end_fill()
        for i in range(side):
            vector.color(COLORS[side - 3])
            vector.forward(length)
            vector.right((360/(side-1))-(360/side))
            recursion(side-1, length/2, fill, COLORS, vector)
            vector.left((360/(side-1))-(360/side))
            vector.left(360/side)

def main():
    randomcolors = [
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
    ]
    tracer(False)
    vector = Turtle()
    vector.penup()
    vector.goto(-200,-200)
    vector.pendown()
    vector.pensize(8)
    recursion(7,200,True,randomcolors,vector)
    update()
    mainloop()


if __name__ == '__main__':
    main()