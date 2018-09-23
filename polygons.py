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
            vector.left(360 / side)
            vector.forward(length)
        if fill:
            vector.end_fill()
        return side * length
    else:
        distance = 0
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
            distance += recursion(side-1, length/2, fill, COLORS, vector)
            vector.left((360/(side-1))-(360/side))
            vector.left(360/side)
        return side*length + distance

def main():
    randomcolors = [
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
        (random(),random(),random()),
    ]
    # tracer(False)
    vector = Turtle()
    vector.speed(0)
    vector.penup()
    vector.goto(-200,-200)
    vector.pendown()
    vector.pensize(2)
    distance = recursion(6,200,False,randomcolors,vector)
    print(distance)
    update()
    mainloop()


if __name__ == '__main__':
    main()