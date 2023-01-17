def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longestPal = ''
    testVal = ''
    for i in range(len(s)):
        testVal += s[i]
        if testVal == testVal[::-1] and len(testVal) > len(longestPal):
            longestPal = testVal
        elif testVal != testVal[::-1]:
            testVal = ''


# Test cases
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
