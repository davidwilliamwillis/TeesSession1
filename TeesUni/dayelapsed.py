#This program will calculate days elapsed between two dates.

xmas_day = 25
xmas_month = 12
xmas_year = 2019

born_day = int(input("Please enter day of month you were born:"))
born_month = int(input("Please enter month you were born in numerical format:"))
born_year = int(input("Please enter year of birth:"))

now_day = int(input("Please enter current day of month:"))
now_month = int(input("Please enter current month:"))
now_year = int(input("Please enter current year:"))


years_indays = (now_year - born_year) *365.25
month_indays = (now_month - born_month) * 30.4 + now_day - born_day
days_born = years_indays + month_indays


years_indays = (xmas_year - now_year) *365.25
month_indays = (xmas_month - now_month) * 30.4 + xmas_day - now_day
days_toxmas = years_indays + month_indays

print ("Approximately ", days_born, " days have elapsed since your birthday! And it is only ", days_toxmas, " days to Xmas!")
