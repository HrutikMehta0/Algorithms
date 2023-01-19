def solution(S, K):
    list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if S in list:
        index = list.index(S)
        return list[(index + K) % 7]


print(solution('Mon', -1))
