
def roomArea () :
    length = int (input ("Please enter room Length:"))
    width =  int (input ("Please enter room width:"))
    area = length*width
    return area

print("Calculating Room 1....")
Room1 = roomArea()

print("Calculating Room 2....")
Room2 = roomArea()

print("Calculating Room 3....")
Room3 = roomArea()

print("Calculating Room 4....")
Room4 = roomArea()

totalArea = Room1 + Room2 + Room3 + Room4
    
print("The area for Room 1 is :", Room1)
print("The area for Room 2 is :", Room2)
print("The area for Room 3 is :", Room3)
print("The area for Room 4 is :", Room4)
print("The total floor area is:", totalArea) 


