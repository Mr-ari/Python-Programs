import turtle

screen = turtle.Screen()
screen.setup(400,400)

turtle = turtle.Turtle()

turtle.penup()

move_speed = 10
turn_speed = 10

def forward():
    turtle.fd(10)

def backward():
    turtle.bk(10)
def left():
    turtle.left(10)
def right():
    turtle.right(10)
    
screen.onkeypress(forward,'Up')
screen.onkeypress(backward,'Down')
screen.onkeypress(left,'Left')
screen.onkeypress(right,'Right')

screen.listen()
