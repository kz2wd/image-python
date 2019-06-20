from PIL import Image
from math import *


def circle(c, r, p=0):  # c => center, r => radius, p => precision
    circle = []
    for i in range(360):
        circle.append((round(cos(i) * r + c[0], p), round(sin(i) * r + c[1], p)))
    return circle


def spiral(c, r, a, length=360, precision=0):  # c => center, r => radius, a => adjustment, l => length p => precision
    spiral = []
    for i in range(length):
        spiral.append((round(cos(i) * (r - i * a) + c[0], precision), round(sin(i) * (r - i * a) + c[1], precision)))
    return spiral


def paint(x, c, p):  # x => objet to paint, c => color, p => pixels grid
    for i in x:
        p[i] = c
    return p


# c1 = circle([100, 100], 50)
# print(c1)

s1 = spiral([250, 250], 150, 0.01, 1000)
print(s1)

im = Image.new('RGB', (500, 500), (255, 0, 0))

pix = im.load()

pix = paint(s1, (0, 255, 255), pix)

im.save("MonImage.png", "PNG")


