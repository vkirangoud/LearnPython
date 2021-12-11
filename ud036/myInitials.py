import turtle

def drawInitials(myTurtle):
    #myTurtle.home()
    
    myTurtle.left(75)
    myTurtle.forward(100)
    myTurtle.home()
    #myTurtle.seth(0)
    myTurtle.left(125)
    myTurtle.forward(100)



def main():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle();
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    points = [[-100, -50], [0, 100], [100, -50]]

    drawInitials(brad)

    window.exitonclick();


main()

    
