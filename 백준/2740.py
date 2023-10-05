# 행렬 곱셈

n,m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

m, k = map(int, input().split())
B = []

for i in range(m):
    B.append(list(map(int, input().split())))

C = [[0]*k for i in range(n)]

for i in range(n):
    for j in range(k):
        C[i][j] = 0
        for t in range(m):
            C[i][j] += A[i][t]*B[t][j]

for element in C:
    print(*element)