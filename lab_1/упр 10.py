import turtle
turtle.speed(10)
turtle.shape('turtle')
for w in range (0,3,1):
    for i in range (0, 180, 1):
        turtle.left(2)
        turtle.forward(3)
    for i in range (0, 180, 1):
        turtle.right(2)
        turtle.forward(3)
    turtle.left(60)
