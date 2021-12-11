# Some experiments with drawing
import turtle

def drawTriangle(points, color, myTurtle):
    #myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    #myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
   # myTurtle.end_fill()
    
def main():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle();
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    points = [[-100, -50], [0, 100], [100, -50]]

    brad.goto(-100, -50)

    drawTriangle(points, "green", brad);

    window.exitonclick();


main()
    
    
