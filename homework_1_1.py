import turtle

window = turtle.Screen()
turtle.reset()

turtle.shape("turtle")
turtle.bgcolor("green")
turtle.color("white")
turtle.speed(1)
turtle.pensize(3)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.left(180)
turtle.forward(105)
turtle.pendown()
turtle.right(30)

turtle.shape("square")
turtle.color("red")
turtle.speed(2)
turtle.pensize(2)

turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

turtle.penup()
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(90)
turtle.right(100)
turtle.pendown()

turtle.shape("circle")
turtle.color("blue")
turtle.speed(3)
turtle.pensize(2)

turtle.circle(50)

window.exitonclick()
