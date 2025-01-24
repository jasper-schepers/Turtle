from turtle import *

from Flags.shapes import rect
from Flags.shapes import centered_star

# zet de neus in de richting als BlocklyGames
left(90)
# traaaaaager
speed(0)

bgcolor('grey')

pensize(25)
penup()

hoogte = 4
breedte = 6

gewenste_hoogte = 321
schaal = gewenste_hoogte / hoogte



# code hier

fillcolor('white')
rect(0, hoogte / 2 * schaal, 6 * schaal, hoogte / 2 * schaal)
fillcolor('#d52b1e')
rect(0, 0, 6 * schaal, hoogte / 2 * schaal)
fillcolor("#0039a6")
rect(0, hoogte / 2 * schaal, 2 * schaal, 2 * schaal)
penup()
# forward(2 / 2 * schaal)
# left(90)
# forward(2 / 2 * schaal)
teleport(1 * schaal, 3 * schaal)
star_size = 1 * schaal
centered_star(star_size, "white", fill=True)







# dit is de laatste lijn
done()
