from turtle import *

from Flags.shapes import centered_circle, rect, n_pointed_star
from utils import is_even

bgcolor('black')

color('white')
speed(0)
hideturtle()

plan_height = 24
plan_width = 48
blue = "#001b69"
yellow = "#ffc828"

drawing_height = 800
scale = drawing_height / plan_height
drawing_width = plan_width * scale

color(blue)
rect(-drawing_width /2, -drawing_height /2, drawing_width, drawing_height)

color(yellow)
yellow_stripe_height = 2 * scale
rect(-drawing_width / 2, - yellow_stripe_height / 2, drawing_width, yellow_stripe_height)

speed(0)

# star
center_x = -12 * scale
center_y = -5 * scale
teleport(center_x, center_y)

n_pointed_star(12, 4 * scale, 2 * scale)


end_fill()

done()
