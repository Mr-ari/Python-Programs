import turtle

def polygon(turtle,color,sides,length,x,y):
    turtle.penup()
    turtle.speed(500)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range (sides):
        turtle.forward(length)
        turtle.left(360/sides)


    turtle.end_fill()
    turtle.hideturtle()
    
        


bob=turtle.Turtle()

polygon(bob,"pink",4,50,0,0)


	
	
