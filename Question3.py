def find_min_days(prices, profit):
    # Participants code will be here
    n = len(prices)
    pr = {}
    
    for i in range(n):
        for j in range(i+1, n):
            x = prices[j] - prices[i] 
            if x > 0:
                if x in pr.keys():
                    if pr[x][1] > j or ( pr[x][1] == j and pr[x][0] < i):
                        pr[x] = [i,j]
                else:
                    pr[x] = [i,j]
    ans = ""
    for x in profit:
        add = ""
        if x in pr.keys():
            add = str(pr[x][0]+1) + " " + str(pr[x][1]+1)
        else:
            add = str(-1)
        if ans == "":
            ans = ans + add
        else:
            ans = ans + ',' + add
    
    return ans


n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this lin