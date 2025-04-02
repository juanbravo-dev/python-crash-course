
# Exercise 5-3 

alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")

alien_color = "green"

if alien_color == "red":
    print("The player just earned 5 points.")

 
    



# Exercise 5-3 (2.0)

import time

alien_color= "green"

guess = input("guess the alien´s color:")
guess= guess.lower()

if guess == "green":
    print("You earned 5 points")

elif guess == "red":
    print("You earned 3 points.")

else:
    for i in range (10):
        print("You´re a loser.")
        time.sleep(1)