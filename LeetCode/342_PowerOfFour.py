import math


def isPowerOfFour(n):
    if n <= 0:
        return False
    else:
        return math.log(n, 4).is_integer()


print(isPowerOfFour(64))
