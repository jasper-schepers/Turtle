from turtle import *

# zet de neus in de richting als BlocklyGames
left(90)
# traaaaaager
speed(0)

bgcolor('black')
pencolor('yellow')
# pensize(2)

# code hier
for i in range(3):
    for _ in range(5):
        forward(50)
        right(144)
    penup()
    forward(150)
    right(120)
    pendown()
left(90)
penup()
forward(100)
pencolor("gray")
pendown()
for w in range(360):
    forward(50)
    backward(50)
    right(1)



# dit is de laatste lijn
done()
