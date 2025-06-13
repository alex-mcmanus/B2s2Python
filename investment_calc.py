#create investment vars
year = 0

#user vars
investment = float(input("what is your IV? £"))

#ensuring investment is a positive number
while True:
    if investment <= 0:
        investment = float(input("please enter positive value or i'll not be happy: "))
    else:
        break 


interest = 1+(float(input("what is your IR in %"))/100)
while True:
    if interest <= 1:
        interest = 1+(float(input("if you put in a negative value you'll literally lose all your money. Put in another value NOW or santa clause will hunt you down: %"))/100)
    else:
        break


target = float(input("what is your target amount? £"))


#print initial condition
print(f'Year {year} - Investment: £{investment:,.2f}')

#while we were below and equal target
while investment <= target:
    print(f'Year {year} - Investment: £{investment:,.2f}')
    year +=1
    investment = (investment * interest)
print('It took ' +str(year)+ ' years to reach the target of ' +str(target), 'the total investment would be £'+str(round(investment,2)))