import math
from turtle import *

from utils import is_even

speed(0)
def rect(left_x, bottom_y, width, height):
    teleport(left_x, bottom_y)
    setheading(0)
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def centered_circle(radius, middle_x, middle_y):
    goto(middle_x, middle_y)
    penup()
    forward(radius)
    left(90)
    pendown()
    circle(radius)
    right(90)
    penup()
    back(radius)

def star_fill(size, color):
    fillcolor(color)
    penup()
    begin_fill()
    for i in range(5):
        forward(size)
        left(4*18)
        forward(size)
        right(144)
    end_fill()
    pendown()

def centered_star(diameter, color, fill=False):
    penup()
    setheading(90)
    forward(diameter/2)
    right(9*18)

    if fill:
        fillcolor(color)
        begin_fill()
    else:
        pendown()
        pencolor(color)

    L = diameter * 0.3632712640
    for i in range(5):
        forward(L)
        left(4*18)
        forward(L)
        right(144)

    if fill:
        end_fill()
    else:
        penup()


    pendown()

def regular_polygon(aantal_hoeken, radius):
    teleport(radius, 0)
    begin_fill()
    for i in range(aantal_hoeken):
        hoek = (i + 1) * 360 / aantal_hoeken
        x = radius * math.cos(math.radians(hoek))
        y = radius * math.sin(math.radians(hoek))
        goto(x, y)
    end_fill()

def n_pointed_star(number_of_spikes, radius_outer, radius_inner):
    number_of_points = 2 * number_of_spikes
    center_x = xcor()
    center_y = ycor()
    teleport(center_x + radius_outer, center_y + 0)
    begin_fill()
    for i in range(number_of_points):
        if is_even(i):
            radius = radius_inner
        else:
            radius = radius_outer

        hoek = (i + 1) * 360 / number_of_points
        x = radius * math.cos(math.radians(hoek))
        y = radius * math.sin(math.radians(hoek))
        goto(center_x + x, center_y + y)
    end_fill()

def polygon(points, scaling, translate=Vec2D(0,0)):
    first_point = points[0]*scaling + translate
    teleport(first_point[0], first_point[1])
    begin_fill()
    for point in points:
        goto(point*scaling + translate)
    end_fill()


if __name__ == "__main__":
    pencolor("red")
    fillcolor("red")
    hoekpunten = [
        Vec2D(0,0),
        Vec2D(0, 6),
        Vec2D(16, 6),
        Vec2D(27, 0),
        Vec2D(0, 0)
    ]

    polygon(hoekpunten, 30, Vec2D(-200, -100))
    done()