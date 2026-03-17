Hawaii_points = 0
Whistler_points = 0
NewYork_points = 0

answer1 = input("Do you prefer A: the beach, B: the mountains, or C: the city?")
if answer1 == "A":
    Hawaii_points += 1
elif answer1 == "B":
    Whistler_points += 1
elif answer1 == "C":
    NewYork_points += 1

answer2 = input("Do you like A: swimming/tanning, B: skiing/snowboarding, or C: shopping/exploring?")
if answer2 == "A":
    Hawaii_points += 1
elif answer2 == "B":
    Whistler_points += 1
elif answer2 == "C":
    NewYork_points += 1

answer3 = input("Do you like A: shaved ice, B: hot chocolate, or C: pizza?")
if answer3 == "A":
    Hawaii_points += 1
elif answer3 == "B":
    Whistler_points += 1
elif answer3 == "C":
    NewYork_points += 1

answer4 = input("Do you like A: sunny weather, B: snowy weather, or C: windy weather?")
if answer4 == "A":
    Hawaii_points += 1
elif answer4 == "B":
    Whistler_points += 1
elif answer4 == "C":
    NewYork_points += 1

answer5 = input("Do you like A: palm trees/sand, B: snow/trees, or C: people/cars")
if answer5 == "A":
    Hawaii_points += 1
elif answer5 == "B":
    Whistler_points += 1
elif answer5 == "C":
    NewYork_points += 1

print(f"Your score is {Hawaii_points} Hawaii, {Whistler_points} Whistler, and {NewYork_points} New York!")