print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
totalbill = 0
if size == "S":
    totalbill += 15
    # print("Your current cost is $" + str(totalbill))
    # print("Your current cost is $",totalbill)
    if pepperoni == "Y":
        totalbill += 2

elif size == "M":
    totalbill += 20
    # print("Your current cost is $",totalbill)
    if pepperoni == "Y":
        totalbill += 3
        # print("Your current cost is $",totalbill)

elif size == "L":
    totalbill += 25
    # print("Your current cost is $",totalbill)
    if pepperoni == "Y":
        totalbill += 3
        # print("Your current cost is $",totalbill)


if extra_cheese == "Y":
    totalbill += 1
print(f"Your final bill is: ${totalbill}.")

