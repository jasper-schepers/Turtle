from turtle import *

# zet de neus in de richting als BlocklyGames
left(90)
# traaaaaager
speed(0)

bgcolor('black')
pencolor('yellow')
# pensize(2)

# code hier
for i in range(4):
    for _ in range(5):
        forward(50)
        right(144)
    penup()
    forward(150)
    right(90)
    pendown()



# dit is de laatste lijn
done()
