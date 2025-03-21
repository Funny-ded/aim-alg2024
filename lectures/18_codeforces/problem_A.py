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
    #n, x = invr()
    
    n = read_int()
    x = read_int()
    
    a = invr()
    
    avg = sum(a) / n
    
    if (avg == x):
        print("YES")
    
    else:
        print("NO")