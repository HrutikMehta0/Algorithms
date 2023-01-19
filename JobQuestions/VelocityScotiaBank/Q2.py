def solution(S):
    removingString = 'BANANA'
    # Frequency of each character in S
    freq = {}
    for i in S:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # Frequency of each character in removingString
    freqBan = {'B': 1, 'A': 3, 'N': 2}
    # Find the minimum number of times we can remove a character from S
    # to make it an anagram of removingString
    min = 0
    # Test to see if the character is in the removingString
    for key in freqBan:
        if key not in freq:
            return 0

    while True:
        for key in freqBan:
            if freq[key] >= freqBan[key]:
                freq[key] -= freqBan[key]
            else:
                return min
        min += 1
    return min


print(solution('BANANA'))
print(solution('NAABXXAN'))
print(solution('BANANAS'))
print(solution('QABAAAWOBL'))
print(solution("NAANAAXNABABYNNBZ"))
print(solution("WSDEBAAANN"))
