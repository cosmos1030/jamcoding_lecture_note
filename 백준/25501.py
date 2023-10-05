import sys

input = sys.stdin.readline

t = int(input())

def recur(string, cnt):
    cnt += 1
    if len(string)==1 or len(string)==0:
        return (1, cnt)
    if string[0] != string[-1]:
        return (0, cnt)
    return recur(string[1:-1], cnt)

for i in range(t):
    temp = input().strip()
    print(*recur(temp, 0))