from random import random, choice, shuffle

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit);

student_scores = [50, 85, 70, 40, 103, 7, 20, 15, 182, 2, 20, 4 ,74]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like to generate?\n'))
nr_symbols = int(input('How many symbols would you like to generate?\n'))
nr_numbers = int(input('How many numbers would you like to generate?\n'))

# Easy Level
password = ''
for i in range(nr_letters):
    password += choice(letters)
for i in range(nr_symbols):
    password += choice(symbols)
for i in range(nr_numbers):
    password += str(choice(numbers))
print(password)

# Hard Level
hardPassword = []
for i in range(nr_letters):
    hardPassword += choice(letters)
for i in range(nr_symbols):
    hardPassword += choice(symbols)
for i in range(nr_numbers):
    hardPassword += str(choice(numbers))
shuffle(hardPassword)
shuffledPassword = ''
for i in hardPassword:
    shuffledPassword += i
print(shuffledPassword)