import math
from turtle import *

from Flags.shapes import centered_circle, rect

bgcolor('gray')
color('white')
green = "#01411C"
speed(0)
hideturtle()
penup()
plan_height = 20
plan_width = 30
plan_white_width = 7 + 1/2
plan_A = math.sqrt((11 + 1/4)**2 + 10**2) - 13
plan_B = 4 - plan_A
plan_center_white_circle_X = (7 + 1/2) + (11 + 1/4)


drawing_height = 600
scale = drawing_height / plan_height
drawing_width = plan_width * scale


fillcolor(green)
rect( (-plan_width / 2) * scale, (-plan_height * scale) / 2, plan_width * scale, plan_height * scale)
fillcolor("white")
rect((-plan_width * scale) / 2, (-plan_height * scale) / 2, plan_white_width * scale, plan_height * scale)


begin_fill()
centered_circle((12 / 2) * scale, (-plan_width / 2 + plan_center_white_circle_X) * scale , 0)
end_fill()

done()


(7+1/2)
