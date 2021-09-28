import turtle
import math
turtle.speed(1)
turtle.shape('turtle')
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.pendown()
def ff(n):
        turtle.left(180/n)
        turtle.forward(2*(50+(i-3)*50)*math.sin(math.pi/n))
        for w in range(0,n-1,1):
            turtle.left(360/n)
            turtle.forward(2*(50+(i-3)*50)*math.sin(math.pi/n))
        turtle.right(90-(180/n))
for i in range(3,10,1):
    ff(i)
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()
