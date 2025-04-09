# 5_6 Stages of life

age = 1

if age < 2:
    print("This person is a baby")

age = 3

if age >= 2 and age < 4:
    print("This person is a toddler")

age = 6

if age >= 4 and age < 13:
    print("This person is a kid")

age = 15

if   13 <= age < 20:
    print("This person is a teenager")

age = 25

if 20 <= age < 65:
    print("This person is an adult")

age = 67

if age >= 65:
    print("This person is an elder")


# Compact version

age = int(input("Enter the person`s age:"))

print("The person is a/an:")

if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")
