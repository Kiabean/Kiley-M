import turtle

screen=turtle.Screen()
screen.screensize(200,200)
screen.bgcolor("light yellow")

t=turtle.Turtle()
t2=turtle.Turtle()
t2.hideturtle()
t2.penup()
t.fillcolor("light pink")
t.begin_fill()
t.pencolor("Black")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Kiley's Slides", font=("arial", 30, "bold"), align = "center")

turtle.addshape("intropic.gif")
t2.goto(-100,0)
t2.shape("intropic.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("intropic2.gif")
t2.goto(150,0)
t2.shape("intropic2.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("light blue")
t.clear()
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()
t=turtle.Turtle()
t.fillcolor("purple")
t.begin_fill()
t.pencolor("white")
t.circle(40)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Foods", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Fries, Chicken nuggets, Mac n Cheese", font=("arial", 30, "bold"), align = "center")

turtle.addshape("fries.gif")
t2.goto(-100,0)
t2.shape("fries.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("macnchees.gif")
t2.goto(150,0)
t2.shape("macnchees.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("light green")

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()

t=turtle.Turtle()
t.fillcolor("white")
t.begin_fill()
t.pencolor("white")
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Hobbies", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Dance, Swimming, Reading, and playing Fortnite ", font=("arial", 15, "bold"), align = "center")

turtle.addshape("dance.gif")
t2.goto(-100,0)
t2.shape("dance.gif")
a = t2.stamp()
t2.goto(-100,0)

turtle.addshape("books.gif")
t2.goto(150,0)
t2.shape("books.gif")
a = t2.stamp()
t2.goto(100,0)

enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("pink")

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()

t=turtle.Turtle()
t.pencolor("Black")
t.fillcolor("aqua")
t.begin_fill()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)

t.left(45)
t.end_fill()
t.penup()
t.goto(0,200)
t.pendown()
t.write("Favorite Movie", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Notebook and High school musical", font=("arial", 30, "bold"), align = "center")

turtle.addshape("Notebook.gif")
t2.goto(-100,0)
t2.shape("Notebook.gif")
a = t2.stamp()
t2.goto(-100,0)


turtle.addshape("Highschoolmusical.gif")
t2.goto(150,0)
t2.shape("Highschoolmusical.gif")
a = t2.stamp()
t2.goto(100,0)


enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


screen.bgcolor("orange")

t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)
t.penup()

t=turtle.Turtle()
t.fillcolor("light yellow")
t.begin_fill()
t.pencolor("white")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.goto(0,200)
t.left(45)
t.end_fill()
t.pendown()
t.write("Favorite Sport", font=("arial", 30, "bold"), align = "center")
t.penup()
t.goto(0,-200)
t.pendown()
t.write("Volleyball", font=("arial", 30, "bold"), align = "center")

turtle.addshape("Volleyball.gif")
t2.goto(-100,0)
t2.shape("Volleyball.gif")
a = t2.stamp()
t2.goto(-100,0)


turtle.addshape("Volleyball2.gif")
t2.goto(150,0)
t2.shape("Volleyball2.gif")
a = t2.stamp()
t2.goto(100,0)


enter=input("Press Enter to continue:")
t.clear()
t2.clearstamps()


