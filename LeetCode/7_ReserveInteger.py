def reverse(x):
    str_x = str(x)
    if str_x[0] == '-':
        str_x = str_x[1:]
        str_x = str_x[::-1]
        str_x = '-' + str_x
    else:
        str_x = str_x[::-1]
    if int(str_x) > 2**31-1 or int(str_x) < -2**31:
        return 0
    return int(str_x)


# Test cases
print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
