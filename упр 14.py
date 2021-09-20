import turtle
turtle.speed(10)
turtle.shape('turtle')
def rf(n):
    for i in range (0, n, 1):
        turtle.left(90-(180/n))
        for r in range (1,n,1):
            turtle.forward(10)
        turtle.left(90)
rf(5)
