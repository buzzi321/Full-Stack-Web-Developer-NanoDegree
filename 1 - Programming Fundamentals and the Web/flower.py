import turtle

def draw_leaf(pen,direction):
    pen.color("green")
    for i in range(1,10):

        if direction == "left":
            pen.lt(10)
        else:
            pen.rt(10)
        pen.fd(10)
    if direction == "left":
        pen.lt(90)
    else:
        pen.rt(90)

    for i in range(1,10):

        if direction == "left":
            pen.lt(10)
        else:
            pen.rt(10)
        pen.fd(10)

def draw_flower(pen,size,color,width):
    pen.color(color)
    pen.width(width)
    pen.speed('fastest')
    for i in range(1, 42):

        for i in range(1,10):
            pen.rt(10)
            pen.fd(size)
        pen.rt(90)
        for i in range(1,10):
            pen.rt(10)
            pen.fd(size)
            pen.rt(1)
def draw_stem(pen):
    for i in range(1,2):
        pen.color("brown")
        pen.fd(200)

def draw():
    window = turtle.Screen()
    window.bgcolor("blue")
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("red")
    pen.width(5)
    pen.speed('slow')
    pen.lt(90)
    draw_stem(pen)
    pen.home()
    pen.lt(90)
    draw_leaf(pen,"left")
    pen.home()
    pen.lt(90)
    pen.fd(30)
    draw_leaf(pen,"right")
    pen.home()
    pen.color("brown")
    pen.lt(90)
    pen.fd(200)
    draw_flower(pen, 10, "red", 3)
    draw_flower(pen,5,"pink",1)
    pen.ht()
    window.exitonclick()
draw()
