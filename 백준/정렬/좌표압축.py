n = int(input())
l = list(map(int, input().split()))
l2 = list(set(l))

l2.sort()

d = {}

for i in range(len(l2)):
    d[l2[i]] = i

for i in l:
    print(d[i], end=" ")