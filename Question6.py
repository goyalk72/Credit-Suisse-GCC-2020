import math
# You may change this function parameters
def encrypt(words):
    # Participants code will be here
    words = words.replace(" ","")
    n = len(words)
    sq = math.sqrt(n)
    c = int(math.ceil(sq))
    f = int(math.floor(sq))
    
    if f * f >= n:
        cut  = f
    else:
        cut = c
            
    ans = ""
    for i in range(cut):
        x = i
        s = ""
        while x < n:
            s = s + words[x]
            x += cut
        if ans == "":
            ans = ans + s
        else:
            ans = ans + " " + s
            
    return ans


def main():
    words = input()

    answer = encrypt(words)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()