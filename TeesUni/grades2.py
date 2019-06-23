

mark = int(input("enter your mark as a whole percent?"))



def getgrade(mark):
    if mark >= 80 and mark <= 100:
        grade = "A*"
    elif mark >= 70 and mark < 80:
        grade = "A"
    elif mark >= 60 and mark < 70:
        grade = "B"
    elif mark >= 50 and mark < 60:
        grade = "C"
    elif mark >= 40 and mark < 50:
        grade = "D"
    elif mark >= 1 and mark < 40:
        grade = "F*"
    elif mark == 0:
        grade = "N/S*"
    return grade   
    
if mark >= 0 and mark <= 100:
    print("You got grade: "+getgrade(mark))
else:
    print ("Please enter a number between 0 and 100")
    
    
    
