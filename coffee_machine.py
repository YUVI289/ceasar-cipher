menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def amount():
    print("Please insert coins.")
    quart = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nick = int(input("How many nickels?: "))
    penn = int(input("How many pennies?: "))
    amt = ((quart*0.25)+(dime*0.1)+(nick*0.05)+(penn*0.01))
    amut = round(amt, 2)
    amut = "{:.2f}".format(amt)
    return amut

def coffee_machine():
    runs = False
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while not runs:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        elif drink in menu:
            item = menu[drink]
            item_ingredients = item['ingredients']
            req_water = item_ingredients['water']
            req_milk = item_ingredients['milk']
            req_coffee = item_ingredients['coffee']
            req_amt = item['cost']
            if req_milk<=milk and req_water<=water and req_coffee<=coffee:
                amt = float(amount())
                if amt<req_amt:
                    print("Sorry that's not enough money. Money refunded.")
                else:    
                    print(f"Here is ${amt-req_amt} in change")
                    print(f"Here is your {drink} Enjoy!")
                    water-=req_water
                    milk-=req_milk
                    coffee-=req_coffee
                    money+=req_amt
            else:
                str1 = ""
                if req_milk>milk:
                    str1+='milk'
                elif req_water>water:
                    str1+='water'
                else:
                    str1+='coffee'
                print(f"Sorry there is not enough {str1}.")
        else:
            print("Fuck You!")
        
        if water<50 or milk==0 or coffee<18:
            print(f"Your profit is ${money}.")
            runs = True

coffee_machine()