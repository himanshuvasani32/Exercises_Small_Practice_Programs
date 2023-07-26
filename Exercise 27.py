import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

# Pick a random int using randrange()
# We add 1 to upper_bound because randrange does not include the upper_bound number.
# random_number = random.randrange(lower_bound, upper_bound + 1)

print(random_number)