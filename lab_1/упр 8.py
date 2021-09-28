import turtle
turtle.speed(100)
turtle.shape('turtle')
def rf(n):
    for i in range (0, n, 1):
        turtle.forward(5+i*5)
        turtle.left(90)

rf(1000)
