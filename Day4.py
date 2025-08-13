import random
# Prints number between 0 and 10
# print(random.randint(0, 10))


# random_num_0_to_1 = random.random() * 10

# Heads or Tails
# random_number = random.randint(0,1)
# if(random_number == 0):
#     print('Heads')
# else:
#     print('tails')

#Lists
# fruits = ['item1', 'item2']
# print(fruits[0])

friends = ['Alice', 'Bob', "Charlie", 'David', 'Emmanuel']
length_of_friends = len(friends)
random_friend = random.randint(0, length_of_friends - 1)
print(friends[random_friend])