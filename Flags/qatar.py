from turtle import *

from Flags.shapes import centered_circle, rect
from utils import is_even

bgcolor('black')

color('white')
speed(0)
hideturtle()

plan_height = 4950
plan_width = 12600
red = "#8A1538"

drawing_height = 800
scaling = drawing_height / plan_height
drawing_width = plan_width * scaling

color(red)
rect(-drawing_width /2, -drawing_height /2, drawing_width, drawing_height)

color('white')
rect(-drawing_width /2, -drawing_height /2, (4200 - 504) * scaling, drawing_height)

speed(0)


hoekpunt_x = (4200 - 504) * scaling - drawing_width / 2
hoekpunt_y = 0 - drawing_height / 2
teleport(hoekpunt_x, hoekpunt_y)
penup()
begin_fill()
for i in range(18):
    hoekpunt_y += 275 * scaling
    if is_even(i):
        # tel 2*504 op bij X
        hoekpunt_x += 2 * 504 * scaling
    else:
        # trek 2*504 af van X
        hoekpunt_x -= 2 * 504 * scaling
    goto(hoekpunt_x, hoekpunt_y)

end_fill()

done()
