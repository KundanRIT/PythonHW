from turtle import *


class Weight:
    __slots__ = "weight"

    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return self.weight


class Beam:
    __slots__ = "weight", "left", "right"

    def __init__(self, weight):
        self.weight = Weight(weight)
        self.left = {}
        self.right = {}

    def insertLeft(self, torque, beam):
        self.weight.weight += beam.weight.weight
        self.left[torque] = beam

    def insertRight(self, torque, beam):
        self.weight.weight += beam.weight.weight
        self.right[torque] = beam

    def height(self, root):
        if len(root.left)== 0 and len(root.right) == 0:
            return 1
        else:
            mx = 0
            for k,v in root.left.items():
                mx = max(mx, self.height(v))
            for k,v in root.right.items():
                mx = max(mx, self.height(v))
            return 1 + mx


def moveR(root):
    max = 0
    if len(root) != 0:
        for k,v in root.items():
            i = k + moveR(v.right)
            if i > max:
                max = i
    return max


def moveL(root):
    max = 0
    if len(root) != 0:
        for k,v in root.items():
            i = k + moveL(v.left)
            if i > max:
                max = i
    return max


# def drawBeam(root, turtle):
#     turtle.pendown()
#     turtle.forward(50)
#     if len(root.left) != 0:
#         turtle.right(90)
#         for k,v in root.left.items():
#             turtle.forward(k*50)
#             turtle.left(90)
#             drawBeam(v, turtle)
#             turtle.left(90)
#             turtle.forward(k*50)
#             turtle.left(180)
#         # turtle.backward(50*(x-2))
#         turtle.left(90)
#     if len(root.right) != 0:
#         # x = moveL(root.right)
#         # turtle.forward(50)
#         turtle.left(90)
#         for k,v in root.right.items():
#             turtle.forward(k*50)
#             turtle.right(90)
#             drawBeam(v, turtle)
#             turtle.right(90)
#             turtle.forward(k*50)
#             turtle.right(180)
#         turtle.right(90)
#     if len(root.left) == 0 and len(root.right) == 0:
#         turtle.write(" " + str(root.weight.weight))
#     turtle.penup()
#     turtle.backward(50)
#     turtle.pendown()


def drawBeam(root, turtle):
    turtle.pendown()
    turtle.forward(50)
    x = max(moveR(root.left), moveL(root.right))
    m = x*10*root.height(root)
    if len(root.left) != 0:
        turtle.right(90)
        for k,v in root.left.items():
            for _ in range(k):
                turtle.forward(m)
                turtle.write("*")
            turtle.left(90)
            drawBeam(v, turtle)
            turtle.left(90)
            turtle.forward(k*m)
            turtle.left(180)
        turtle.left(90)
    if len(root.right) != 0:
        # x = moveL(root.right)
        # turtle.forward(50)
        turtle.left(90)
        for k,v in root.right.items():
            # x = moveL(root.right)
            # m = x * 50
            for _ in range(k):
                turtle.forward(m)
                turtle.write("*")
            turtle.right(90)
            drawBeam(v, turtle)
            turtle.right(90)
            turtle.forward(k*m)
            turtle.right(180)
        turtle.right(90)
    if len(root.left) == 0 and len(root.right) == 0:
        turtle.write(" " + str(root.weight.weight))
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()


def main():
    beams = {}
    with open("beam.txt") as f:
        for line in f:
            entries = line.strip().split()
            name = entries[0]
            aBeam = Beam(0)
            for i in range(1, len(entries), 2):
                node = entries[i+1]
                if node not in beams:
                    beam = Beam(int(node))
                else:
                    beam = beams[node]
                torque = int(entries[i])
                if torque <= 0:
                    aBeam.insertLeft(abs(torque), beam)
                else:
                    aBeam.insertRight(abs(torque), beam)
            beams[name] = aBeam
    root = beams["B"]
    turtle = Turtle()
    # tracer(False)
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.left(180)
    # root.right = {}
    drawBeam(root, turtle)
    # print(root.height(root.right[1]))
    # update()
    mainloop()


if __name__ == '__main__':
    main()

    # B1 -2 6 -1 3 3 5
    # B2 -1 4 1 2 2 1
    # B3 -1 B2 1 7
    # B -1 B1 1 B3
