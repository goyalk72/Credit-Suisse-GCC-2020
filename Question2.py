# You may change this function parameters
def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    # Participants code will be here
    profit = 0
    buy = 0
    while buy < numOfPredictedTimes:
        bought = False
        Sold = False
        while buy + 1 < numOfPredictedTimes and predictedSharePrices[buy] > predictedSharePrices[buy+1]:
            buy += 1
        if buy < numOfPredictedTimes:
            bought = True
        sell = buy + 1
        if sell >= numOfPredictedTimes:
            return profit
        while sell + 1 < numOfPredictedTimes and predictedSharePrices[sell] < predictedSharePrices[sell+1]:
            sell += 1
        if sell < numOfPredictedTimes:
            Sold = True
        if bought and Sold:
            profit += predictedSharePrices[sell] - predictedSharePrices[buy]
        buy = sell + 1
    return profit


def main():
    line = input().split()
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()