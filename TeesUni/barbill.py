# Automatic bar bill calculator
# Pete 19/09/2017
# Saul 06/05/2019

# Initial bar price list
price_magners = 2.75
price_aftershock = 3.00
price_vodka = 3.00
price_redbull = 2.50
price_coke = 10.00

print("Hi. I'm Erica - your automated barmaid for the evening!")

bottles = input("How many bottles of Magners did you drink? ")
bottles = int(bottles)
cost = bottles * price_magners
print("Wow - you can knock 'em back. You spend ", cost, " pounds on booze")

number = int(input("How many vodka and redbulls did you drink"))
cost = number * (price_vodka + price_redbull)
print("That'll give you wings! You spent ", cost, "quid.")

# Is the above correct? Test it out!
