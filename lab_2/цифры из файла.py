import turtle as t

t.shape('turtle')
      
crr=open('crr.txt','r')
massiv=[]
a=-1
b=-1
for i in range(0,10):
    vString=crr.readline()
    listdig=[]
    for j in range(len(vString)):
        if vString[j]=="(":
            a=int(j) 
        elif vString[j]==")":
            b=int(j)
        if a!=-1 and b!=-1:
            List=tuple(map(int, vString[a+1:b].split(",")))
            listdig.append(List)
            a=-1
            b=-1
    massiv.append(listdig)
crr.close()

print(massiv[1])
def f(A):
    for x, y in A:
         if x == 0 and y == 0: t.penup()
         if x == 1 and y == 0: t.pendown()
         t.forward (x)
         t.right(y)
    t.penup()
    t.forward (10)
    t.pendown()
            
f(massiv[1])
f(massiv[4])
f(massiv[1])
f(massiv[7])
f(massiv[0])
f(massiv[0])
