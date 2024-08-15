# 실전 18-4 행성 터널


# =============
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
x = []
y = []
z = []
for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0], x[i+1][1], x[i][1]))
    edges.append((y[i+1][0]-y[i][0], y[i+1][1], y[i][1]))
    edges.append((z[i+1][0]-z[i][0], z[i+1][1], z[i][1]))
edges.sort()

parents = [i for i in range(n)]
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        result += cost
        union_parent(parents, a, b)

print(result)