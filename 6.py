import random


def generate_random_list(list_lenght):
    random_list = []
    for i in range(random.randint(0, list_lenght)):
        n = random.randint(0, 9)
        random_list.append(n)
    return random_list


lenght = int(input())
print(generate_random_list(lenght))
