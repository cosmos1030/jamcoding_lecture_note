n = int(input())
l= []
for i in range(n):
    age, name = input().split()
    age = int(age)
    l.append([age, name])

l = sorted(l, key=lambda x:x[0])

for i in l:
    print(i[0], i[1])