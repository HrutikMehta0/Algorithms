def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longestPal = ''
    start = 0
    end = 0
    if s is None or len(s) < 1:
        return longestPal
    for i in range(len(s)):
        len1 = expandMiddle(s, i, i)
        len2 = expandMiddle(s, i, i + 1)
        lenMax = max(len1, len2)
        if lenMax > end - start:
            start = i - (lenMax - 1) // 2
            end = i + lenMax // 2
    return s[start:end + 1]


def expandMiddle(s, left, right):
    if s is None or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


# Test cases
print(longestPalindrome("babad"))  # b ba bab
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
