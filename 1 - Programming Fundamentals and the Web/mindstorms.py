import turtle
window = turtle.Screen()
window.bgcolor("skyblue")
def draw_square():
    i=0
    window = turtle.Screen()
    window.bgcolor("skyblue")
    brad = turtle.Turtle()
    brad.color("red","yellow")
    brad.shape("turtle")
    brad.speed(20)
    for a in range(1,100):
        i=0
        while i < 4:
            brad.forward(100)
            brad.right(90)
            i = i+1
        brad.right(5)
'''def draw_circle():
    angie = turtle.Turtle()
    angie.shape("classic")
    angie.color("brown")
    angie.speed(2)
    angie.circle(100)
def draw_triangle():
    sam = turtle.Turtle()
    sam.speed(2)
    sam.shape("classic")
    sam.color("blue")
    i=0
    sam.right(100)
    while i < 3:
        sam.forward(100)
        sam.right(120)
        i = i+1'''
draw_square()
#draw_circle()
#draw_triangle()
window.exitonclick()