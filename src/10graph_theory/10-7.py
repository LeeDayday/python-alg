# 예제 10-7 도시 분할 계획


# =============
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a

def solution():
    n, m = map(int, input().split())
    costs = []
    total_cost = 0
    max_cost = 0
    parent = [i for i in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        costs.append((c, a, b))

    costs.sort()

    for i in range(m):
        cost, a, b = costs[i]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            max_cost = cost
            
    print(total_cost - max_cost)


if __name__ == '__main__':
    solution()