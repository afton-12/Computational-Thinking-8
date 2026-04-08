# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("nyc")

s1 = create_sprite("dog", -200, 0)
s2 = create_sprite("cool_dog", 200, 0)

s1.color("blue")
s2.color("dark red")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("On the moon!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s2.write("No I have not!", font = ("Arial", 20, "normal"))
window.update()
s2.clear()
######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()