# 실전 18-3 어두운 길


# =============
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
edges = []
parent = [i for i in range(n+1)]

for _ in range(m):
    x, y, w = map(int, input().split())
    edges.append((w, x, y))

edges.sort()
total = 0 # 전체 가로등 설치  (최악의 경우)
result = 0 # 최소 설치 비용 (최적의 경우)
# 간선을 최소비용 순으로 확인
for edge in edges:
    w, x, y = edge
    total += w
    # 사이클이 발생하지 않는 경우에만 트리 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += w

print(total - result)