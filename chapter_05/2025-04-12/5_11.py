# Ordinal Numbers

numbers = list(range(1,10))

for number in numbers:
    if number == (1):
        print(f"{number}st")
    elif number == (2):
        print(f"{number}nd")
    elif number == (3):
        print(f"{number}rd")
    else: 
        print(f"{number}th")


# Another solution, printing a list
my_list = []

for i in range (1,10):
    my_list.append(i)

formatted_list = []

for number in my_list:
    if number == (1):
        formatted_list.append("1st")
    elif number == (2):
        formatted_list.append("2nd")
    elif number == (3):
        formatted_list.append("3rd")
    else: 
        formatted_list.append(f"{number}th")

print(my_list)