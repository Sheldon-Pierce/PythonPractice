# thing = 2 + 2
# if thing:
#     # do this
#     print("Thing is true")
# else:
#     # do this
#     print("Thing is false")

# Even or Odd problem

# user_input = int(input('Odd or Even? Provide a number: '))
# if user_input % 2 == 0:
#     print('Your number is even')
# else:
#     print('Your number is odd')

# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M or L: ')
# pepperoni = input("Do you want perpperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == 'S':
#     bill = 15
#     if pepperoni == 'Y':
#         bill += 2
#     if extra_cheese == 'Y':
#         bill += 1
# elif size == 'M':
#     bill = 20
#     if pepperoni == 'Y':
#         bill += 3
#     if extra_cheese == 'Y':
#         bill += 1
# elif size == 'L':
#     bill = 25
#     if pepperoni == 'Y':
#         bill += 3
#     if extra_cheese == 'Y':
#         bill += 1
# else:
#     print("You typed the wrong inputs")
# print(f'Your final bull is: ${bill}.')

# Logical Operators

# a = 12

# a > 10 and a < 15
# #Returns true

# a > 10  and a < 11
# #returns false

# a > 10 or a < 4
# #returns true

print("Welcome to treasure island. Your mission is to find the treasure.")
first_answer = input('Choose a path').lower()
if(first_answer == 'left'):
    second_answer = input('wait or swim').lower()
    if(second_answer == 'wait'):
        third_answer = input('Choose a door color: red, yellow or blue').lower()
        if(third_answer == 'yellow'):
            print('You Win!')
        else:
            print('Game Over.')
    else:
        print('Game Over.')
else:
    print('Game Over.')