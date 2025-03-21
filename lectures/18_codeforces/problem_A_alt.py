import sys

input = sys.stdin.readline

def read_int():
    return int(input())
     
def invr():
    return(map(int,input().split()))
     
def insr():
     s = input()
     return(list(s[:len(s)-1]))
     
t = read_int()

for _ in range(t):
     n, x = invr()
     s = insr()
     Sum = 0
     for i in range(len(s)):
          Sum += s[i]
     
     if (Sum == n*x):
          print('Yes')
     else:
          print('No')