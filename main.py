
import random


def generate_random_list(list_length):
    random_list = []
    for i in range(random.randint(0, list_length)):
        n = random.randint(0, 9)
        random_list.append(n)
    return random_list


length = int(input())
print(generate_random_list(length))
