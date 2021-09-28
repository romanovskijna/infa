import turtle as tr
t0=116
tr.speed(0)
tr.shape('circle')

c=0
k=1
p=0
f=0
for t in range (0, t0, 1):
    x = (10/k)*(t-f)+c
    y =(60/k)*(t-f)-(1/2)*2*(t-f)**2
    if y<=0:
        k=k+1
        f=t
        c=x
        tr.goto(x,y)
    else:
        x = (10/k)*(t-f)+c
        y =(60/k)*(t-f)-(1/2)*2*(t-f)**2
        tr.goto(x,y)
