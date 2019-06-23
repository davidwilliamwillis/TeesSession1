import math

def sphere(r):
    area = math.pi*(r**2)*(4/3)
    return area



def cylinder(r,h):
    area = math.pi*(r**2)*h
    return area



def cone (r,h):
    area = (1/3) * math.pi * (r**2) * h
    return area




##will repeat till number chosen
def choosenumber():
    number = input()
    try:
        return int(number)
    except:
        print ("try again")
        choosenumber()



    

##prints menu
print("1 Find area of a sphere")
print("2 Find area of a cylinder")
print("3 Find area of a cone")
choice = choosenumber()
if choice == 1:
    print("You chose sphere")
    print("What is the radius")
    radius = choosenumber()
    print(sphere(radius))
elif choice== 2:
    print("You chose cylinder")
    print("What is the radius")
    radius = choosenumber()
    print("What is the height")
    height = choosenumber()
    print (cylinder(radius, height))
elif choice ==3:
    print("You chose cone")
    print("What is the radius")
    radius = choosenumber()
    print("What is the height")
    height = choosenumber()
    print (cone(radius, height))
else:
    print("invalid choice")
    
    
    
    
    
        



      
