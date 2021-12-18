import random

users = ["Azri", 'Fatihah', "Susanto", "Radit", "Ilham"]

# lower_index = 0
# higher_index = len(users) - 1

# random_int = random.randint(lower_index, higher_index)

# winner = users[random_int]

# print(winner)

winner = random.choice(users)
print(winner)