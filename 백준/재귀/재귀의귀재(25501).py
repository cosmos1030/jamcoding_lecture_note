import sys
input = sys.stdin.readline

def is_palin(s, cnt):
    if len(s)==1 or len(s)==0:
        return (1, cnt)
    if s[0] != s[-1]:
        return (0, cnt)
    return is_palin(s[1:-1], cnt+1)

t = int(input())

for i in range(t):
    s = input().strip()
    result = is_palin(s, 1)
    print(result[0], result[1])
