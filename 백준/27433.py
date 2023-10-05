n = int(input())

def recur(num):
    if num==0:
        return 1
    return num*recur(num-1)

print(recur(n))