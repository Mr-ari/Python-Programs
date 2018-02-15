import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()


tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(5)   
tommy.penup()
draw_circle(tommy, "green", 50, 0, 0)
draw_circle(tommy, "blue", 50, -50, 0)
draw_circle(tommy, "yellow", 50, -100, 0)

tommy.penup()
tommy.goto(-25,-50)
tommy.color("black")
tommy.write("aww!Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(-25,-80)
