import turtle

tom=turtle.Turtle()

face_color="yellow"
eye_one="white"
eye_two="black"

tom.speed(10)
tom.pensize(2)
tom.pencolor("black")
tom.color(face_color)
tom.penup()
tom.goto(0,-150)
tom.pendown()
tom.begin_fill()
tom.circle(200)
tom.end_fill()
tom.color(eye_one)
tom.penup()
tom.goto(-85,90)
tom.begin_fill()
tom.circle(40)
tom.end_fill()
tom.color(eye_two)
tom.begin_fill()
tom.circle(20)
tom.end_fill()
tom.color(eye_one)
tom.penup()
tom.goto(85,90)
tom.begin_fill()
tom.circle(40)
tom.end_fill()
tom.color(eye_two)
tom.begin_fill()
tom.circle(20)
tom.end_fill()
tom.penup()
tom.goto(-50,-40)
tom.color(eye_one)
tom.begin_fill()
tom.left(270)
tom.circle(50,180)
tom.left(90)
tom.forward(100)
tom.end_fill()
tom.penup()
tom.goto(0,75)
tom.color("red")
tom.begin_fill()
tom.pendown()
tom.circle(40)
tom.end_fill()
tom.hideturtle()






