from turtle import *
import math

# totie
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)



### Write your code below:
color = input('choose a color for shape1: ')
color2 = input('choose a color for shape2: ')
sidenumber = int(input('how many sides will the shape have:'))
print('now watch them')

pencolor(color)
pendown()
for sides in range(sidenumber):
    forward(50)
    right(360/sidenumber)
penup()



pencolor(color2)
goto(150,0)
pendown()
for tsides in range(3):
    forward(50)
    right(120)
penup()






# Close window on click.
exitonclick()
