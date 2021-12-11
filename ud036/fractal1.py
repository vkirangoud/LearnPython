# Serpensiki Triangle 
import turtle

def drawTriangle(points, myTurtle, fillFlag):
    if fillFlag == True:
        myTurtle.fillcolor("white")
    else:
        myTurtle.fillcolor("green")
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()

    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])

    myTurtle.end_fill()

def getMid(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def sierpinski(points, degree, myTurtle, fillFlag):
    drawTriangle(points, myTurtle, fillFlag)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0],points[1]),
                    getMid(points[0],points[2])],
                   degree-1, myTurtle, 0)
        
        sierpinski([points[1],
                    getMid(points[1],points[0]),
                    getMid(points[1],points[2])],
                   degree-1, myTurtle, 0)

        sierpinski([points[2],
                    getMid(points[1],points[2]),
                    getMid(points[0],points[2])],
                   degree-1, myTurtle, 0)

        print ("Level " + str(degree) +" Flag = "+str(fillFlag) )
    
def main():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle();
    brad.shape("turtle")
    brad.color("black")
    brad.speed(1)

    points = [[-100, -50], [0, 100], [100, -50]]

    fillflag = 1

    
    sierpinski(points, 3, brad, fillflag)

    window.exitonclick();


main()
    
    
