def partitionString(s):
        curSet = set()
        res = 1
        for c in s:
            if c in curSet:
                res += 1
                curSet = set()
            curSet.add(c)
        return res


# Test cases
print(partitionString("abac"))
print(partitionString("abacaba"))
print(partitionString("ssssss"))