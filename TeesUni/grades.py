

mark = int(input("enter your mark as a whole percent?"))



if mark >= 80 and mark <= 100:
    print("A*")
elif mark >= 70 and mark < 80:
    print("A")
elif mark >= 60 and mark < 70:
    print("B")
elif mark >= 50 and mark < 60:
    print("C")
elif mark >= 40 and mark < 50:
    print("D")
elif mark >= 1 and mark < 40:
    print("F")
elif mark == 0:
    print("N/S")
else:
    print("Requires a whole number between 0 and 100")


    
    


