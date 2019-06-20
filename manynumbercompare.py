
#declaring empty variables here
number1 = ""
number2 = ""

##first line checks variable from last run wont run if last one was a quit, valiable need to be declared out side loop otherwise dont exist
while number1 != "quit" and number2 != "quit":
    number1 = input("Please enter a number")
    number2 = input("Please enter a number")
##run this good bye message if user has typed quit    
    if number1 == "quit" or number2 == "quit":
        print("Goodbye")
    else:
        print(number1 + number2)
        number1=int(number1)
        number2=int(number2)
        if number1 > number2:
            print("Number 1 is the greatest")
        elif number2 > number1:
            print("Number 2 is the greatest")
        else:
            print("They are both the same")





    
