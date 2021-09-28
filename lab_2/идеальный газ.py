from random import randint
import turtle
import numpy as np


number_of_turtles = 10
steps_of_time_number = 20000

turtle.penup()
turtle.forward (200)
turtle.pendown()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
for i in range (0,4,1):
    turtle.forward(400)
    turtle.left(90)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
x = np.random.randint(-200, 200, number_of_turtles)
y = np.random.randint(-200, 200, number_of_turtles)
print(x)
u=0
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.goto(x[u],y[u])
    u=u+1
vx = np.random.randint(0, 40, number_of_turtles )
vy = np.random.randint(40, 80, number_of_turtles )
print(vx)    

for j in range(steps_of_time_number):
    p=0
    for unit in pool:
        x[p]=x[p]+vx[p]*0.05
        y[p]=y[p]+vy[p]*0.05
        if x[p]>190:
            vx[p]=-vx[p]
        if x[p]<-190:
            vx[p]=-vx[p]
        if y[p]<-190:
            vy[p]=-vy[p]
        if y[p]>190:
            vy[p]=-vy[p]
        unit.goto(x[p],y[p])
        p=p+1
        # for unit2 in pool:
           # if (unit.xcor()-unit2.ycor())**2<100 and unit!=unit2:
                #vx[p]=vx[i]
                #vx[i]=vx[p]
           # if (unit2.xcor()-unit.xcor())**2<=100 and unit!=unit2:
                #vy[p]=vy[i]
                #vy[i]=vy[p]
print(vx)
   
        
