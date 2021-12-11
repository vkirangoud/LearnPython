import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create the turtle Brad - Draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)
    

    window.exitonclick()

draw_art()

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)
    
    for x in range(1,5):
        brad.forward(100)
        brad.right(90)
    
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)
    #brad.right(90)
    #brad.forward(100)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #draw triangle
    beige = turtle.Turtle()
    beige.shape("square")
    beige.color("white")
    beige.speed(1)
    beige.forward(100)
    beige.left(90)
    beige.forward(100)
    beige.left(135)
    beige.forward(141)
    
    
    window.exitonclick()

#draw_shapes()
    
