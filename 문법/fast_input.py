n = int(input())
l = list(map(int, input().split()))

min = 1234567891
max = -1234567891

for element in l:
    if element<min:
        min = element
    if element > max:
        max = element

print(min, max)