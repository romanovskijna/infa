import turtle
turtle.speed(100)
turtle.shape('turtle')
def rf(n):
    for i in range (0, n, 1):
        turtle.forward(50)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(50)
        turtle.left(180-(360/n))

rf(10)
