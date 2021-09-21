import turtle
turtle.speed(100)
turtle.shape('turtle')

turtle.begin_fill()
for i in range (0, 180, 1):
    turtle.left(2)
    turtle.forward(5)
turtle.fillcolor('yellow')
turtle.end_fill()

turtle.penup()
turtle.goto(50,150)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor('black')
for i in range (0, 180, 1):
    turtle.left(2)
    turtle.forward(0.8)
turtle.end_fill()
    
turtle.penup()
turtle.goto(-50,150)
turtle.pendown()

turtle.begin_fill()
turtle.fillcolor('black')
for i in range (0, 180, 1):
    turtle.left(2)
    turtle.forward(0.8)
turtle.end_fill()
    
turtle.penup()
turtle.goto(0,130)
turtle.pendown()

turtle.width(12)
turtle.right(90)
turtle.forward(30)

turtle.penup()
turtle.goto(-30,60)
turtle.pendown()

turtle.pencolor('red')
for i in range (0, 90, 1):
    turtle.left(2)
    turtle.forward(1)

