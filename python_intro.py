# # el mejores mesanges del mundo
# message = 'Bon'

# name = input('What is your name?')

# print(message)

# print ('Hello '+name)

#A very simple for loop (the most complex for loop ever created)

# food = ['carrot', 'eggs', 'bread','spaghetti', 'orange']

# for item in food:
#     if item == 'eggs':
#         print('I do not like '+item)
#     elif item == 'orange':
#         print('I like an '+item)
#     else:
#         print('I love '+item)


#very simple while loop

# x = 0

# while x <=10:
#     print(x)
#     x+=1

#more complex example
# from datetime import datetime
# from datetime import timedelta

# start = input('Pick a start date in a proper format or bad things will occur ')
# end = input('Pick and end date in proper format or bad things will occur ')

# start = datetime.strptime(start, "%Y-%m-%d")
# end = datetime.strptime(end, "%Y-%m-%d")

# while start <= end:
#     print(start)
#     start = start + timedelta(days=1)

#maybe more useful example
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