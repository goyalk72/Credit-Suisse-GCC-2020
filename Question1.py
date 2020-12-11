import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    maxsofar = 0
    sumsofar = 0
    for i in range(1,numOfPredictedDay):
        diff = predictedSharePrices[i] - predictedSharePrices[i-1]
        sumsofar = max(diff + sumsofar, 0)
        maxsofar = max(maxsofar,sumsofar)
    return maxsofar


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()
