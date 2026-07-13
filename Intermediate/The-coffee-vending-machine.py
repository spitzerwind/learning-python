MENU = {
    "espresso": {
        "ingredients": {
            "water": 250,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def payment_gateway(pymnt):
    qtrs= int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))


    total_money = (qtrs*0.25 + dimes*0.10 + nickels*0.05 + penny*0.01)
    print(f"Your coins in total $:{total_money}")


    if total_money >= pymnt:
        change = round(total_money-pymnt,2)
        print(f"Transaction succesfull here is your change: ${change}")
        return True
    else:
        print(f"Transaction failed here is your refund: ${total_money}")
        return False

def coffee_making(flavour):
    if flavour == "espresso":
        print(f"Please insert coins your total is ${MENU['espresso']['cost']}")
        Price = MENU['espresso']['cost']

        if payment_gateway(Price) == True:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            resources["money"] += MENU["espresso"]["cost"]


            print("Here is your espresso ☕️. Enjoy!")
    elif flavour == "latte":
        print(f"Please insert coins your total is ${MENU['latte']['cost']}")
        Price = MENU['latte']['cost']

        if payment_gateway(Price) == True:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["money"] += MENU["latte"]["cost"]

            print("Here is your latte ☕️. Enjoy!")
    elif flavour == "cappuccino":
        print(f"Please insert coins your total is ${MENU['cappuccino']['cost']}")
        Price = MENU['cappuccino']['cost']

        if payment_gateway(Price) == True:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["money"] += MENU["cappuccino"]["cost"]
            print("Here is your cappuccino ☕️. Enjoy!")


machine_status = True

while machine_status:

    User_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()


    if User_coffee == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print(f"Sorry, We don't have enough water")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, we don't have enough coffee")
        else:
            coffee_making("espresso")




    elif User_coffee == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print(f"Sorry, We don't have enough water")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, we don't have enough coffee")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, we don't have enough milk")
        else:
            coffee_making("latte")





    elif User_coffee == "cappuccino":

       if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
           print(f"Sorry, We don't have enough water")
       elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
           print("Sorry, we don't have enough coffee")
       elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
           print("Sorry, we don't have enough milk")
       else:
            coffee_making("cappuccino")

    elif User_coffee == "off":
        machine_status = False



    elif User_coffee == "report":
        print(f"water : {resources['water']}\nmilk : {resources['milk']}\ncoffee : {resources['coffee']}\nmoney: ${resources["money"]}")




    else:
        print("Please insert correct input")




