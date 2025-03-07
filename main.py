import turtle

screen = turtle.Screen()
screen.screensize(500, 500)
t = turtle.Turtle()
t.speed(0)
screen.bgcolor('Tan')

t.penup()
t.pencolor('Blue')
t.goto(-80, 15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('Black')
t.goto(0, 15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('Red')
t.goto(80, 15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('Yellow')
t.goto(-40, -10)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('Green')
t.goto(40, -10)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.goto(0,100)
t.pencolor("Purple")
t.write( 'Winter Olympics', font=("Arial", 30, "bold"), align="center")
t.penup()

t.penup()
t.goto(0,-100)
t.pencolor("Purple")
t.write( '2026', font=("Arial", 30, "bold"), align="center")
t.penup()


#This is the last line of code
turtle.done()