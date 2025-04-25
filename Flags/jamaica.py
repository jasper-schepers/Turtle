import math
from turtle import *
from shapes import polygon, rect



penup()
bgcolor("gray")
black = "#000000"
green = "#007847"
yellow = "#FFB915"
a = math.sqrt(0.5**2 + 0.25**2)
a = math.sqrt(1**2 + 0.5**2)
scale = 50

flag_width_on_plan = 12
flag_height_on_plan = 6



speed(0)
fillcolor(black)
rect( 0, 0, flag_width_on_plan*scale, flag_height_on_plan*scale)

hoekpunten = [
        Vec2D(0,0),
        Vec2D(flag_width_on_plan/2, flag_height_on_plan/2),
        Vec2D(flag_width_on_plan, 0),
        Vec2D(0, 0)
]
fillcolor(green)
polygon(hoekpunten, scale)

hoekpunten = [
        Vec2D(0,flag_height_on_plan),
        Vec2D(flag_width_on_plan/2, flag_height_on_plan/2),
        Vec2D(flag_width_on_plan, flag_height_on_plan),
        Vec2D(0, flag_height_on_plan)
]
fillcolor(green)
polygon(hoekpunten, scale)

hoekpunten = [
        Vec2D(0,flag_height_on_plan),
        Vec2D(flag_width_on_plan/2, flag_height_on_plan/2),
        Vec2D(flag_width_on_plan, flag_height_on_plan),
        Vec2D(0, flag_height_on_plan)
]
fillcolor(green)
polygon(hoekpunten, scale)


done()
