import random

random_double = random.random()
random_int = random.randint(1, 100)
choice_numbers = [4, 8, 52, 98]
random_choice_number = random.choice(choice_numbers)

print('Random double : {}'.format(random_double))
print('Random  int : {}'.format(random_int))
print('Random  choice : {}'.format(random_choice_number))