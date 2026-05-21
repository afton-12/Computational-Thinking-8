from utils import *
import random
#The goal of the game is to get as many waters as possible!
# Section 1 - setup
# TODO - set a background using set_background()
set_background("capybara_sunset")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
flowers = 0
water = 0

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_flower():
    global flowers
    flowers += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("flower",x,y)
def get_water():
    global flowers, water
    if flowers >= water*2+2:
        water += 1
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("waterbottle",x,y)

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(get_flower, "f")

# TODO - make a second control
window.onkeypress(get_water, "w")





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    m1.clear()
    m1.write(f"Water: {water}\nFlower: {flowers}",font=("Arial",30,"normal"))   
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # m1.clear()
    # m1.write("Hello")

    time.sleep(0.01)
    window.update()