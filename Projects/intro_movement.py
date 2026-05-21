import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("cardinal2",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+10)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-10)
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-10, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+10, y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

def draw():
    s1.pendown()
window.onkeypress(draw, "c")

def stop_drawing():
    s1.penup()
window.onkeyrelease(stop_drawing, "c")

def erase():
    s1.clear()
window.onkeypress(erase, " ")

def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "r")

def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "g")

def reset():
    s1.goto(0,0)
window.onkeypress(reset, "z")

s2 = create_sprite("cool_dog",0,-200)

# Section 2: define controls
def move_upp():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y+10)
        
def move_downn():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y-10)
    
def move_leftt():
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x-10, y)
    
def move_rightt(): 
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x+10, y)

window.onkeypress(move_upp, "1")
window.onkeypress(move_downn, "2")
window.onkeypress(move_leftt, "3")
window.onkeypress(move_rightt, "4")

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()