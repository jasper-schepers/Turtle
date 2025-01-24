from turtle import *
from shapes import polygon
penup()
bgcolor("gray")
blue = "#00205B"
red = "#BA0C2F"
scale = 10

speed(0)

hoekpunten = [
        Vec2D(0,0),
        Vec2D(0, 6),
        Vec2D(16, 6),
        Vec2D(27, 0),
        Vec2D(0, 0)
]
fillcolor(red)
polygon(hoekpunten, scale, Vec2D(-200, -100))
Vec2D(0, 0)

hoekpunten = [
        Vec2D(0, 10),
        Vec2D(0, 16),
        Vec2D(27, 16),
        Vec2D(16, 10),
        Vec2D(0, 10)
    ]
fillcolor(red)
polygon(hoekpunten, scale, Vec2D(-200, -100))
hoekpunten = [
        Vec2D(0, 6),
        Vec2D(0, 10),
        Vec2D(16, 10),
        Vec2D(27, 8),
        Vec2D(16, 6),
        Vec2D(0, 6)
    ]
fillcolor("white")
polygon(hoekpunten, scale, Vec2D(-200, -100))

hoekpunten = [
        Vec2D(6, 16),
        Vec2D(10, 16),
        Vec2D(10, 0),
        Vec2D(6, 0),
        Vec2D(6, 16),
    ]
fillcolor("white")
polygon(hoekpunten, scale, Vec2D(-200, -100))
hoekpunten = [
        Vec2D(0, 7),
        Vec2D(0, 9),
        Vec2D(21.5, 9),
        Vec2D(27, 8),
        Vec2D(21.5, 7),
        Vec2D(0, 7)
    ]
fillcolor(blue)
polygon(hoekpunten, scale, Vec2D(-200, -100))
hoekpunten = [
        Vec2D(7, 16),
        Vec2D(9, 16),
        Vec2D(9, 0),
        Vec2D(7, 0),
        Vec2D(7, 16),
    ]
fillcolor(blue)
polygon(hoekpunten, scale, Vec2D(-200, -100))


done()
