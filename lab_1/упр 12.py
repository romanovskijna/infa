import turtle
turtle.speed(100)
turtle.shape('turtle')
turtle.left(90)
for w in range (0,10,1):
    for i in range (0, 180, 1):
        turtle.right(1)
        turtle.forward(1)
    for i in range (0, 180, 1):
        turtle.right(1)
        turtle.forward(0.09)
    
