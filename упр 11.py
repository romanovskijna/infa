import turtle
turtle.speed(1000)
turtle.shape('turtle')
turtle.right(90)
for w in range (0,10,1):
    for i in range (0, 36, 1):
        turtle.left(10)
        turtle.forward(w+10)
    for i in range (0, 36, 1):
        turtle.right(10)
        turtle.forward(w+10)
