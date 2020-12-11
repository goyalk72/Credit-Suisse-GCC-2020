# Participants may update the following function parameters
def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):
    #return -1
    arr = []
    for i,j,k in zip(p,x,y):
        ans = (i * j * 100) - ((100 - i*100) * k)
        arr.append(ans)
    arr.sort(reverse = True)
    expected = 0
    for i in range(maximumTradesAllowed):
        if arr[i] >= 0:
            expected += arr[i]
        else:
            break
    if expected % 100 == 0:
        return str(expected/100) + "0"
    elif expected % 10 == 0:
        return str(expected/100) + "0"
    else:
        return str(round(expected/100,2))

def main():
    # This part may require participants to fill in as well.
    noOfTradesAvailable, maximumTradesAllowed = list(map(int, input().split()))
    p = list(map(float, input().split()))
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    # Participants may update the following function parameters
    answer = maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()