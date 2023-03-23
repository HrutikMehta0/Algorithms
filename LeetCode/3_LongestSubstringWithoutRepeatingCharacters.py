def lengthOfLongestSubstring(s):
    maxLength = 0
    startIndex = 0
    endIndex = 0
    temp = ''
    while endIndex < len(s):
        while startIndex < endIndex and s[endIndex] in temp:
            temp = temp.replace(s[startIndex], '')
            startIndex += 1
        temp += s[endIndex]
        maxLength = max(maxLength, len(temp))
        endIndex += 1
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
