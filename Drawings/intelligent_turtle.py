import turtle


tom=turtle.Turtle()
sc=turtle.Screen()

answer=int(input("what is 100*2??"))

if answer==200:
    tom.penup()
    tom.goto(0,0)
    tom.write("Answer is correct")
    tom.hideturtle()


else:
    sc.bgcolor("red")
    tom.write("your Answer is not correct")
    tom.hideturtle()




    
