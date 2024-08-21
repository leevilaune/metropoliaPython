from random import random, randint


def generate_code(amount, range_min, range_max):
    code = ""
    for amount in range(amount):
        code += str(randint(range_min,range_max))
    return code

print("Koodi 3 nro:",generate_code(3,1,9))
print("Koodi 4 nro:",generate_code(4,1,6))
