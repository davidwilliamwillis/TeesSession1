def roomVolume () :
    length = int (input ("Please enter room Length:"))
    width =  int (input ("Please enter room width:"))
    height =  int (input ("Please enter room height:"))
    volume = length*width*height
    return volume

print("Calculating Room 1....")
Room1 = roomVolume()

print("Calculating Room 2....")
Room2 = roomVolume()

print("Calculating Room 3....")
Room3 = roomVolume()

print("Calculating Room 4....")
Room4 = roomVolume()

totalVolume = Room1 + Room2 + Room3 + Room4
    
print("The volume for Room 1 is :", Room1)
print("The volume for Room 2 is :", Room2)
print("The volume for Room 3 is :", Room3)
print("The volume for Room 4 is :", Room4)
print("The total floor volume is:", totalVolume) 
