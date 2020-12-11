import collections
# Participants may update the following function parameters
def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    sus = [0]*10000
    visited = [0]*10000
    
    qanda = {}
    answer = {}
    
    maxn = 0
    for qa in questionAndAnswerListOfList:
        q = qa[0]
        l = len(qa)
        maxn = max(q,maxn)
        for i in range(1,l):
            a = qa[i]
            if a not in answer:
                answer[a] = []
            answer[a].append(q)
            if (a,q) in qanda:
                sus[q] = 2
                sus[a] = 2
            qanda[(q,a)] = 1
            maxn = max(a,maxn)
            
    for i in range(maxn+1):
        change = 0
        for u in answer:
            if sus[u] < 2 or visited[u] == 1:
                continue
            visited[u] = 1
            change += 1
            for v in answer[u]:
                sus[v] += 1
        if change == 0:
            break
        
    ans = ""
    for i in range(1,maxn+1):
        if sus[i] >= 2:
            ans = ans + str(i) + ","
    if ans == "":
        return ""
    return ans[:-1]
                    


def main():
    firstLine = input().split(" ")
    secondLine = input()

    # Sample input:
    # 3
    # 1 2,2 1,3 1 2

    numOfQuestions = int(firstLine[0])
    questionAndAnswers = secondLine.split(",")
    questionAndAnswerListOfList = parseQuestionAndAnswer(questionAndAnswers)

    # Participants may update the following function parameters
    answer = findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parseQuestionAndAnswer(questionAndAnswers):
    questionAndAnswerListOfList = []
    for index in range(0, len(questionAndAnswers)):
        questionAndAnswerList = questionAndAnswers[index].split(" ")
        questionAndAnswerListOfList.append([int(x) for x in questionAndAnswerList])
    return questionAndAnswerListOfList


if __name__ == '__main__':
    main()