import math

def pythagoras(distance_x, distance_y):
    return math.sqrt(distance_x, distance_y)

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0