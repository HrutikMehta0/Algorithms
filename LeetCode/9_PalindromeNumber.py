def isPalindrome(x):
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1]