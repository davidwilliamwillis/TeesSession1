

first_num = (int(input("Please enter first number:")))
second_num = (int(input("Please enter second number:")))
third_num = (int(input("Please enter third number:")))

list =[]

if first_num < second_num and first_num < third_num:
    list.append(first_num)
    if second_num < third_num:
        list.append(second_num)
        list.append(third_num)
    else:
        list.append(third_num)
        list.append(second_num)
elif second_num < first_num and second_num < third_num:
    list.append(second_num)
    if first_num < third_num:
        list.append(first_num)
        list.append(third_num)
    else:
        list.append(third_num)
        list.append(first_num)
else:
    list.append(third_num)
    if first_num < second_num:
        list.append(first_num)
        list.append(second_num)
    else:
        list.append(second_num)
        list.append(first_num)

print (list)
        
        
        
        

    


        


