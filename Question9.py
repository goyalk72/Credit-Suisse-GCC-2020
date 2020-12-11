def organizingContainers(container):
    # Participants code will be here
    n = len(container)
        
    rowsum = [0]*n
    colsum = [0]*n
    
    for i in range(n):
        for j in range(n):
            rowsum[i] += container[i][j]
            colsum[j] += container[i][j]

    for i in range(n):
        if rowsum[i] != colsum[i]:
            return "Impossible"
            
    return "Possible"
            

if __name__ == "__main__":
    q = int(input().strip())
    answer=""
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        if(answer == ""):
             answer = str(result)
        else:
            answer = answer +  "," +str(result)
    # Do not remove below line
    print(answer)    
    # Do not print anything after this line