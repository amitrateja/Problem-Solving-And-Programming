import turtle 
a=turtle.Turtle()
turtle.bgcolor("midnightblue")
clr=["aquamarine","cyan","deep sky blue"]
a.speed(0)

for i in range(500):
    a.color(clr[i%3])
    a.forward(i)
    a.left(122)
    
    
a.hideturtle()
turtle.exitonclick()
    
