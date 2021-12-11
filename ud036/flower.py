import turtle

def draw_rhombus_1(myTurtle, ln):
    angle = 45
    tog   = True
    for i in range(1,5):
        if tog == True:
            myTurtle.right(90-angle)
            myTurtle.forward(ln)
            tog = False
        else:
            myTurtle.right(90+angle)
            myTurtle.forward(ln)
            tog = True

def draw_rhombus(myTurtle, ln):
    angle = 45
    tog   = True
    for i in range(1,5):
        if tog == True:
            myTurtle.forward(ln)
            myTurtle.right(90-angle)            
            tog = False
        else:
            myTurtle.forward(ln)
            myTurtle.right(90+angle)            
            tog = True


def draw_flower():
    wnd = turtle.Screen()
    wnd.bgcolor("red")

    # Create turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    brad.seth(270)

    for x in range(1,37):
        draw_rhombus(brad, 100)
        brad.right(10)

    brad.forward(500)

    wnd.exitonclick()


draw_flower()
