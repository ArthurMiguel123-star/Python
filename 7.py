import turtle


win = turtle.Screen()
win.bgcolor('black')


heart = turtle.Turtle()
heart.speed(1)  
heart.color('pink')

def draw_heart(t):
    t.begin_fill()  
    t.left(140)
    t.forward(180)
    t.circle(-100, 200)
    t.left(120)
    t.circle(-100, 200)
    t.forward(180)
    t.end_fill()  

draw_heart(heart)

turtle.done()
