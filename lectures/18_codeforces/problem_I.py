import sys

input = sys.stdin.readline

def read_int():
    return int(input())

def invr():
    return(map(int,input().split()))

def insr():
    s = input()

    return (list(s[:len(s) - 1]))

t = read_int()

for _ in range(t):
    n, k = invr()
    
    x = invr()
    
    srt = sorted(x)
    
    arr = srt

    i, j = 0, len(arr) - 1

    score = 0
    
    while(i < j):
        el_sum = arr[i] + arr[j]
        
        if (el_sum == k):
            score += 1
            i += 1
            j -= 1
        
        elif (el_sum > k):
            j -= 1
        
        else:
            i += 1
    
    print(score)
