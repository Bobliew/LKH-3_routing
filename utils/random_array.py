import random

def generate_2d_array(n):
    array = [[random.randint(1, 10), random.randint(1, 10)] for _ in range(n)]
    return array
