n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append((a,b))
l = sorted(l, key=lambda element: (element[0], element[1]))
for element in l:
    print(element[0], element[1])