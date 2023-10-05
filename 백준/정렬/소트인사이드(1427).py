n = input()
l = []
for i in n:
    l.append(i)
l.sort(reverse=True)
for i in l:
    print(i, end="")