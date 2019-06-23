# Student Marks Administration
# Pete Dwyer 01/11/17
# Saul Johnson 20/06/2019

from datafile import data

# Initialise variables.

# Define functions.
def show_raw_data(dat):
   for ind in range(0, len(dat), 2):
       print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4)) 




##workd out grading
def grading(score):
   if score >=70:
      return 'Distinction'
   elif score >=60:
      return 'Merit'
   elif score >=40:
      return 'Pass'
   else:
      return 'Fail'


##will print out names and grades(not needed but making this helped me get to next stage)
def showgrade(dat):
   for ind in range(0, len(dat), 2):
       print(dat[ind].ljust(10), grading((dat[ind + 1])).rjust(4))

##will print out pass list with nmae, score grade
def passlist(dat):
   for ind in range(1, len(dat), 2):
      if dat[ind] > 39:
         print(dat[ind - 1].ljust(10), str(dat[ind]).rjust(4), "    ",grading(dat[ind]))



## finds resit students  
def resubmission(score):
   if score < 40 and score >= 30:
      return True
   else:
      return False

def resitList(dat):
   print("The following students have failed but are entitled to a resubmission:")
   for ind in range(1, len(dat), 2):
      if resubmission(dat[ind]) == True:
         print(dat[ind - 1].ljust(10))

def highestMark(dat):
   for ind in range(1, len(dat), 2):
      if dat[ind] == max(dat[1::2]):
         print(dat[ind - 1].ljust(10), str(dat[ind]).rjust(4))
   
def lowestMark(dat):
   for ind in range(1, len(dat), 2):
      if dat[ind] == min(dat[1::2]):
         print(dat[ind - 1].ljust(10), str(dat[ind]).rjust(4))

def fullrange(dat):
   print("The lowest score was: ", str(min(dat[1::2])))
   print("The highest score was: ", str(max(dat[1::2])))



fullrange(data)


def averageMark(dat):
   count=0
   allmarks = 0
   for ind in range(1, len(dat), 2):
      allmarks = allmarks + dat[ind]
      count = count+1
   return allmarks/count

   
def abovebelowAverage(dat):
   above = 0
   below = 0
   for ind in range(1, len(dat), 2):
      if dat[ind] > averageMark(dat):
         above = above+1
         
      elif dat[ind] < averageMark(dat):
         below = below+1
   return [below, above]

         
         
   






# Main body of program.
show_raw_data(data)




print("Passlist")
passlist(data)

resitList(data)

print("Highest Mark:")
highestMark(data)

print("Lowest mark:")
lowestMark(data)



   
print("The average score was", str(averageMark(data)))
print ('the number of students below average was ', str((abovebelowAverage(data))[0]), ' the number above average was', str((abovebelowAverage(data))[1]))

