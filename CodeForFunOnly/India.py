import turtle 
t = turtle.Turtle()
bg = "cyan"
s = turtle.Screen().bgcolor(bg)
p=turtle.Turtle()


p.penup()
p.goto(-600,225)
p.pendown()
p.color("blue")
p.right(90)
p.begin_fill()
p.forward(150)
p.left(90)
p.forward(40)
p.left(90)
p.forward(150)
p.end_fill()
p.ht()


pen = turtle.Turtle()
pen.penup()
pen.goto(-400,75)
pen.pendown()
# Defining a method to draw curve
def curve():
    for i in range(200):
  
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.fillcolor('red')
  
    # Start filling the color
    pen.begin_fill()
  
    # Draw the left line
    pen.left(140)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    pen.forward(112)
  
    # Ending the filling of the color
    pen.end_fill()
  
  

heart()
pen.ht()



t.color(bg)
t.goto(-250,225)

# I
t.color("Orange")
t.right(90)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(40)
t.left(90)
t.forward(150)
t.end_fill()

t.penup()
t.goto(-170,75)
t.pendown()

# N
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(30)
t.right(45)
t.forward(100*(2**.5)-10)
t.left(135)
t.forward((100*(2**.5)-10)/(2**.5))
t.right(90)
t.forward(30)
t.right(90)
t.forward(150)
t.right(90)
t.forward(30)
t.right(45)
t.forward(100*(2**.5)-10)
t.left(135)
t.forward((100*(2**.5)-10)/(2**.5))
t.end_fill()



t.penup()
t.goto(10,225)
t.pendown()

# D
t.left(90)
t.color("white")
t.right(90)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(150)
t.end_fill()
t.begin_fill()
t.left(90)
t.circle(75,-180)
t.end_fill()

t.goto(40,100)
t.color(bg)
t.begin_fill()
t.circle(50,180)
t.end_fill()

t.penup()
t.goto(140,225)
t.pendown()
# I
t.color("green")
t.left(90)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(40)
t.left(90)
t.forward(150)
t.end_fill()


t.penup()
t.goto(280,225)
t.pendown()
# A
t.begin_fill()
t.right(90)
t.forward(50)
t.right(60)
t.forward(150*2/(3**.5))
t.right(120)
t.forward(40)
t.right(60)
t.forward(45)
t.left(60)

t.penup()
t.goto(280,225)
t.pendown()
t.left(60)
t.forward(150*2/(3**.5))
t.left(120)
t.forward(40)
t.left(60)
t.forward(45)
t.goto(354.10,113.97)
t.end_fill()
t.penup()
t.color(bg)
t.begin_fill()
t.goto(339.10,139.95)
t.pendown()
t.left(60)
t.forward(60)
t.left(120)
t.forward(60)
t.goto(339.10,139.95)
t.end_fill()
t.ht()








turtle.done()