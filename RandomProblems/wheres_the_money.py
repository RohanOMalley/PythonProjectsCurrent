###
### Author: Rohan O'Malley
### Course:CSc 110
### Description: User can input their expenses and a print out will show how much their spend compared to their salary
### shows visuals and will let them know if they are over budget or how much extra money they have
import os
print('-----------------------------')
print("----- WHERE'S THE MONEY -----")
print('-----------------------------')
# Main input statements for user
salary=input('What is your annual salary?\n')
if salary.isnumeric() != True:
    print('Must enter positive integer for salary.')
    os._exit(0)
mortgage=(input('How much is your monthly mortgage or rent?\n'))
if mortgage.isnumeric() != True:
    print('Must enter positive integer for mortgage or rent.')
    os._exit(0)
bills_payment=(input('What do you spend on bills monthly?\n'))
if bills_payment.isnumeric() != True:
    print('Must enter positive integer for bills.')
    os._exit(0)
grocery=(input('What are your weekly grocery/food expenses?\n'))
if grocery.isnumeric() != True:
    print('Must enter positive integer for food.')
    os._exit(0)
travel_expenses=(input('How much do you spend on travel annually?\n'))
if travel_expenses.isnumeric() != True:
    print('Must enter positive integer for travel.')
    os._exit(0)
print(' ')

# changing the strings to floats so they work in the equations

salary=float(salary)
mortgage=float(mortgage)
bills_payment=float(bills_payment)
grocery=float(grocery)
travel_expenses=float(travel_expenses)

# if statements to find what percent of tax should be taken out of salary

if salary <= 15000:
    tax_percentage= 0.1

elif salary <= 75000:
    tax_percentage= 0.2

elif salary <= 200000:
    tax_percentage = 0.25

else:
    tax_percentage= 0.3


annual_salary_tax= (salary*tax_percentage)

# the tax cap if salary is too high

if annual_salary_tax >=75000:
    annual_salary_tax= 75000

total_expenses=(mortgage*12+bills_payment*12+grocery*52+travel_expenses+annual_salary_tax)
extra_value=salary-total_expenses

#percentages for the inputs for column 3

mortgage_percent= round(((mortgage*12)/salary)*100,1)
bills_percent= round(((bills_payment*12)/salary)*100,1)
grocery_percent= round(((grocery*52)/salary)*100,1)
travel_percent= round((travel_expenses/salary)*100,1)
annual_tax_percent= round((annual_salary_tax/salary)*100,1)
extra_percent= round((extra_value/salary)*100,1)

# the amount of dashes for the seperations between the lines

maxium_dashs=int(max(mortgage_percent, bills_percent,grocery_percent,travel_percent,\
annual_tax_percent,extra_percent))

new_salary=int(salary)

print('------------------------------------------'+'-'*maxium_dashs)
print('See the financial breakdown below, based on a salary of $'+str(new_salary))
print('------------------------------------------'+'-'*maxium_dashs)
print('| mortgage/rent | $',format(mortgage*12,'10,.2f')+' |',(format(mortgage_percent,'5,.1f'))+'% | '+'#'*int(mortgage_percent))
print('|         bills | $',format(bills_payment*12,'10,.2f')+' |',(format(bills_percent,'5,.1f'))+'% | '+'#'*int(bills_percent))
print('|          food | $',format(grocery*52,'10,.2f')+' |',(format(grocery_percent,'5,.1f'))+'% | '+'#'*int(grocery_percent))
print('|        travel | $',format(travel_expenses,'10,.2f')+' |',(format(travel_percent,'5,.1f'))+'% | '+'#'*int(travel_percent))
print('|           tax | $',format(annual_salary_tax,'10,.2f')+' |',format(annual_tax_percent,'5,.1f')+'% | '+'#'*int(annual_tax_percent))
print('|         extra | $',format(extra_value,'10,.2f')+' |',format(extra_percent,'5,.1f')+'% | '+'#'*int(extra_percent))
print('------------------------------------------'+'-'*maxium_dashs)

# warning statements if restrictions are met

if extra_value < 0:
    print('>>> WARNING: DEFICIT <<<')
if annual_salary_tax >= 75000:
    print('>>> TAX LIMIT REACHED <<<')