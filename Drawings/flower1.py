import turtle

t=turtle.Turtle()
t.pensize(30)
t.speed(50)
colors=["violet","blue","green","yellow","orange","red","pink"]

for i in range (150):
    t.color(colors[i%7])
    t.fd(2+i*5)
    t.left(45)

    

