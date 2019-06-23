import random

##a function that simulates roll of 2 dice
def diceRoll():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  return dice1 + dice2

##a list to be amend alternating dice out come and number times rolled  
diced=[2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0]


##function that does 100 rolls, on each roll it will add 1 to the number next to the number on list it throws 
def hundred(outcomes):
  n=0
  while n<101:
    roll=diceRoll()
    for o in range(0, len(outcomes), 2):
      if roll == outcomes[o]:
        outcomes[o+1]= 1+outcomes[o+1]    
    n = n+1
##final part will print results
  print("Score: Rolls: ")
  for o in range(0, len(outcomes), 2):   
    print(str(outcomes[o]).ljust(4) ,  str(outcomes[o + 1]).ljust(3), ('*'*(outcomes[o + 1])))  




hundred(diced)

print(diced)
