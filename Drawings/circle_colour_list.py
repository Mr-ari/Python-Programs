import turtle

tom=turtle.Turtle()

color_list=["purple","pink","red","yellow","green","blue","orange","black"]

tom.speed(50)
tom.pensize(3)
tom.speed(200)
for color in color_list:
    angle=360/(len(color_list))
    tom.color(color)
    tom.circle(50)
    tom.begin_fill()
    tom.circle(30)
    tom.end_fill()
    tom.right(angle)
    tom.forward(30)

    
    
