import math
def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    else:
        return math.log(n, 4).is_integer()


print(isPowerOfFour(64))