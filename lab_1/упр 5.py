import turtle
turtle.speed(100)

turtle.shape('turtle')
for i in range (1, 10, 1):
    turtle.forward(50*i)
    turtle.left(90)
    turtle.forward(50*i)
    turtle.left(90)
    turtle.forward(50*i)
    turtle.left(90)
    turtle.forward(50*i)
    turtle.right(45)
    turtle.penup()
    turtle.forward(50*2**(1/2)/2)
    turtle.left(135)
    turtle.pendown()
