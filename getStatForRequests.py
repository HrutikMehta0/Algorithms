def getStatForRequests(m, database, requests):
    output = {}
    finalOutput = []
    for i in range(0, len(database)):
        databaseSplit = database[i].split(" ")
        request = databaseSplit[1]
        if request not in output:
            output[request] = []
        output[request].append([databaseSplit[0], databaseSplit[2]])
    userCount = []
    for i in range(0, m):
        userCount.append(0)
    for i in range(0, len(requests)):
        url = output[requests[i]][0][1]
        intVal = int(output[requests[i]][0][0])
        userCount[intVal] += 1
        finalOutput.append([url, str(userCount[intVal])])
    print(finalOutput)
    return finalOutput






m = 3
database = ["0 sdsf www.google.com", "1 juytf www.google.com", "0 opoit www.kaggle.com"]
requests = ["juytf", "sdsf", "opoit"]
getStatForRequests(m, database, requests) # [['www.google.com', '1'], ['www.google.com', '0'], ['www.kaggle.com', 0']]
m = 3
database =["0 glggl www.google.com", "0 fcbok www.facebook.com", "2 lefts www.hackerrank.com", "0 hckrk www.hackerrank.com"]
requests = ["hckrk", "lefts"]
getStatForRequests(m, database, requests) # [['www.hackerrank.com', '0'], ['www.hackerrank.com', '2']]
