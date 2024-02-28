def findJudge(n, trust):
    dict_trust = {}
    for i in range(1, n+1):
        dict_trust[i] = 0
    i = 0
    while i < n:
        if trust[i][0] == 1:
            dict_trust[trust[i][1]] += 1
        elif trust[i][0] == 2:
            dict_trust[trust[i][1]] += 1



findJudge(2, [[1,2]])

