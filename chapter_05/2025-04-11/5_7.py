# Favorite fruits

favorite_fruits = ["Apple", "Banana", "Watermelon", "Kiwi", "Pineapple"]

if "Apple" in favorite_fruits:
    print("You really like apples!")

if "Banana" in favorite_fruits:
    print("You really like bananas!")

if "Watermelon" in favorite_fruits:
    print("You really like watermelons!")

if "Kiwi" in favorite_fruits:
    print("You really like kiwis!")

if "Pineapple" in favorite_fruits:
    print("You really like pineapples!")


 # Improved version

import inflect

p = inflect.engine()

for fruit in favorite_fruits:
    fruit_plural = p.plural(fruit)
    print(f"You really like {fruit_plural}!")


