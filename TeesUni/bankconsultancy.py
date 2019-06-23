
##asking questions to get data
creditScore = int(input("Please enter creditscore 1 -10:"))
addressTerm = int(input("How many months at current address"))
income = int(input("What is the income level (£)"))
loanRequest = int(input("Borrowing amount requested (£)"))

##this is a variable that would go to true if loan approved
Loan = False

##scenario 0 outright decline
if creditScore == 0 and addressTerm == 0:
    print("loan is declined")
##scenario 1 on worksheet
elif loanRequest > income and loanRequest < (2 * income):
    if addressTerm >= 60 and creditScore >= 5:
        Loan = True
        print("loan approved")
    else:
        print("loan is declined")
##scenario 2 on worksheet        
elif loanRequest < income:
    if addressTerm > 12 and addressTerm < 60:
        if creditScore >= 7 and creditScore <= 10:
            Loan = True
            print("loan approved")
        else:
            print("loan is declined")
##scenario 3            
    elif addressTerm >= 60:
        if creditScore >= 2 and creditScore <= 5:
            Loan = True
            print("loan approved")
        else:
            print("loan is declined")
##scenario 3            
elif loanrequest < 0.2 * income:
    if creditScore == 1 and addressTerm > 12:
        Loan = True
        print("loan approved")
        
else:
    print("loan declined")
        
        
        
            
            
            
        
        
    
        
