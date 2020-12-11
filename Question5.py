# cook your dish here
# You may change this function parameters
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):
    edgesb = [0]*(numOfBankers+1)
    edgesp = [0]*(numOfParticipants+1)
    ans = 0
    Pref = {}
    
    for i in range(1,numOfParticipants+1):
        p = participantsPreferences[i-1]
        for x in p:
            x = int(x)
            Pref[(x,i)] = 1
            edgesb[x] += 1
            edgesp[i] += 1
            ans = max(ans, edgesp[i], edgesb[x])
    for i in range(1,numOfBankers+1):
        p = bankersPreferences[i-1]
        for x in p:
            x = int(x)
            if (i,x) in Pref:
                continue
            Pref[(i,x)] = 1
            edgesb[i] += 1
            edgesp[x] += 1
            ans = max(ans, edgesp[x], edgesb[i])
    
    return ans



def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(firstLine[0])
    numOfParticipants = int(secondLine[0])
    bankersPreferences = firstLine[1].split(",")
    participantsPreferences = secondLine[1].split(",")

    bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    participantsPreferencesListOfList = parsePreferences(participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parsePreferences(preferences):
    preferenceListOfList = []
    for index in range(0, len(preferences)):
        preferenceArr = preferences[index].split("&")
        preferenceListOfList.append([int(p) for p in preferenceArr])
    return preferenceListOfList


if __name__ == '__main__':
    main()
