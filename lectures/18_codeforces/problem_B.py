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
    l, r, d, u = invr()
    
    if (l == r and d == u and l == u):
        print("YES")
    
    else:
        print("NO")