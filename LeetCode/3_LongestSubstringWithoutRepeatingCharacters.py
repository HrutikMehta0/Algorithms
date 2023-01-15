def lengthOfLongestSubstring(s):
    maxLength = 0
    startIndex = 0
    endIndex = 0
    temp = ""
    while endIndex < len(s):
        endIndex += 1
        if s[startIndex] not in temp:
            while startIndex < endIndex and s[startIndex] not in temp:
                temp += s[startIndex]
                startIndex += 1
                maxLength = max(maxLength, len(temp))
    return maxLength
# def lengthOfLongestSubstring(s):
#     max = 0
#     for i in range(0, len(s)):
#         chars = []
#         temp = ""
#         if s[i] not in chars:
#             for j in range(i, len(s)):
#                 if s[j] not in chars:
#                     temp += s[j]
#                     chars.append(s[j])
#                     if len(temp) > max:
#                         max = len(temp)
#                 else:
#                     i = j
#                     break
#     return max


print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
