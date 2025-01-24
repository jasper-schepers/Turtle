from turtle import *

from Flags.shapes import centered_circle, rect

bgcolor('black')

color('white')
speed(0)
hideturtle()

height = 300
scaling = height / 60
width = 100 * scaling

color("#DA291C")
rect(0, 0, width, height)

color('white')

rect(0, 0, 25 * scaling, height)

speed(0)

hoekpunten = [
(25, 0),
(40, 6),
(25, 12),
(40, 18),
(25, 24),
(40, 30),
(25, 36),
(40, 42),
(25, 48),
(40, 54),
(25, 60)
]



teleport(hoekpunten[0][0] * scaling , hoekpunten[0][1] * scaling)
begin_fill()
for punt in hoekpunten:
    goto(punt[0] * scaling, punt[1] * scaling)
end_fill()

done()
