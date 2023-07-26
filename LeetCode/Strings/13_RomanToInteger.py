def romanToInt(s):
    romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(0, len(s)):
        if i - 1 >= 0 and romanDict.get(s[i - 1]) < romanDict.get(s[i]):
            result += romanDict.get(s[i]) - (romanDict.get(s[i - 1]) * 2)
        else:
            result += romanDict.get(s[i])
    return result


### Test ###
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("IV"))
