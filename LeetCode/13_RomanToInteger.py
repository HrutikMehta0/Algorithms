def romanToInt(s):
    romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(0, len(s)):
        result += romanDict.get(s[i])
        if i - 1 > 0 and s[i - 1] < s[i]:
            result -= romanDict.get(s[i - 1]) * 2
    return result


### Test ###
print(romanToInt("IV"))
# print(romanToInt("MCMXCIV"))
