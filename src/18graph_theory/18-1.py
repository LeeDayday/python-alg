# 실전 18-1 여행 계획



# =============
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
parent = [i for i in range(n)] # parent 배열. 자기 자신으로 초기화

for _ in range(n):
    graph.append(list(map(int, input().split())))

data = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, i, j):
    i = find_parent(parent, i)
    j = find_parent(parent, j)
    if i < j:
        parent[j] = i
    elif j > i:
        parent[i] = j

for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] == 1:
            union_parent(parent, i, j)

tmp = find_parent(parent, data[0])
for i in range(1, m):
    if tmp != find_parent(parent, data[i]):
        print("NO")
        exit(0)
print("YES")