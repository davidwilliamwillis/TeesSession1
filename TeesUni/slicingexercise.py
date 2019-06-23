import random

rucksack = ['Water flask', 'Cheese', 'Gold coins', 'Handkercheif', 'Tinderbox',
            'Scrolls', 'Dagger','Rope','Nuts','Pipe','Tobacco','Wine skin',
            'Herbs','Axe']


##function to sort inventory, printout and print number of items
def rucksackupdate():
    rucksack.sort()
    print(rucksack)
    print (str(len(rucksack)), "items in rucksack")


##function to remove item from list by a random indexnumber
def thief(inventory):
    itemremoved = inventory.pop(random.randint(0,len(inventory)-1))
    print ("A thief has stolen your", itemremoved)


rucksackupdate()



treasurechest = ['Gems', 'Necklace']



rucksack = rucksack + treasurechest

rucksackupdate()

## 5 items stolen
thief(rucksack)
thief(rucksack)
thief(rucksack)
thief(rucksack)
thief(rucksack)




rucksackupdate()




