print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("youth tickets are $7.")
        bill = 7
    else:
        print("adult tickets are $12.")
        bill = 12
    userpics = input("if you wish to have photos for 3$ extra type'y' else type 'n' for opting out")
    if userpics == "y":
        bill += 3
    print("your bill is:"+"$",bill)

else:
    print("Sorry you have to grow taller before you can ride.")
