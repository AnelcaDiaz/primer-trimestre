#Animacion
import turtle

screen=turtle.Screen()
screen.bgcolor("thistle")

t=turtle.Turtle()
t.speed(0)

t.color("red")
t.begin_fill()

t.left(148)
t.forward(113)

for _ in range(200):
    t.right(1)
    t.forward(1)
    
t.left(120)

for _ in range(200):
    t.right(1)
    t.forward(1)
    
t.forward(112)

t.end_fill()
t.setpos(0,-22)
t.color("black")
t.hideturtle()
t.write("Bo Go Ship Da",align="center",font=("Nicolk",17,"bold"))
turtle.done() 