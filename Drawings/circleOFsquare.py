import turtle

t=turtle.Turtle()

def square(length):
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)

color_list=["blue","yellow","green","red","violet","pink","orange","black"]

t.speed(5000)
t.pensize(2)

for i in range (0,len(color_list)):
    l=(360*(i+1))/20
    t.pencolor(color_list[i])
    for j in range (int (l)):
        square(150)
        t.left(20/(i+1))
        
        

    
    
    
    
    
