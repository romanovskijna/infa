import turtle as tr
from random import *
tr.speed(0)
tr.shape('turtle')
for i in range(1,1000,1):
    x=randint(1,100)
    y=randint(1,360)
    tr.forward(x)
    tr.left(y)
