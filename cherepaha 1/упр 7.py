import turtle
turtle.speed(100)
turtle.shape('turtle')
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.pendown()
for i in range (0, 360, 1):
    turtle.left(10)
    turtle.forward(0.05*i)

