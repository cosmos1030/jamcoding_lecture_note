n = int(input())
l = []
for i in range(n):
    temp = input()
    if temp not in l:
        l.append(temp)
l = sorted(l)
l = sorted(l, key=lambda x:len(x))
for i in l:
    print(i)