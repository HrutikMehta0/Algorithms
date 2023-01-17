def myAtoi(s):
    str_s = ''
    if not s[0].isdigit() and s[0] != '-' and s[0] != '+' and s[0] != ' ':
        return 0
    for i in range(len(s)):
        if s[i] != ' ' and s[i] == '-' or s[i] == '+' or s[i].isdigit():
            str_s += s[i]
    if int(str_s) > 2**31-1:
        return 2**31-1
    elif int(str_s) < -2**31:
        return -2**31
    return int(str_s)


# Test cases
print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
