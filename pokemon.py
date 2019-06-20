
##I wanted to simplify entering it so i print a menu and get them choose coorrsponing number
print ("Choose your type of Pokemon")
print ("For Fire press 1")
print ("For Water press 2")
print ("For Grass press 3")
print ("For Electric press 4")



type = int(input("Make your selection:"))
letter = str(input("Whats the first letter of your Pokemons name:"))

##to make it easier for variations in case I'm turning all string to capital
letter = letter.capitalize() 


if type == 1 and letter == "C":
    print("You chose Fire, your pokemon is called Charmander")
elif type == 1 and letter == "M":
    print("You chose Fire, your pokemon is called Moltres")    
elif type == 2 and letter == "S":
    print("You chose Water, your pokemon is called Squirtle")
elif type == 2 and letter == "T":
    print("You chose Water, your pokemon is called Tentacool")
elif type == 3 and letter == "B":
    print("You chose Grass, your pokemon is called Bulbassaur")   
elif type == 3 and letter == "O":
    print("You chose Grass, your pokemon is called Oddish")    
elif type == 4 and letter == "P":
    print("You chose Electric, your pokemon is called Pikachu ")
elif type == 4 and letter == "V":
    print("You chose Electric, your pokemon is called Voltorb")
else:
    print("Sorry I can't guess")

    
