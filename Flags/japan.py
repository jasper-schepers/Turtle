from turtle import *

from Flags.shapes import centered_circle, rect

bgcolor('black')

color('white')
speed(0)

height = 300
width = height / 2 * 3

rect(-width / 2, - height / 2, width, height)

teleport(0, 0)

color('#a8323a')

penup()
home()
begin_fill()
centered_circle(height * 3 / 5 / 2)
end_fill()


done()
