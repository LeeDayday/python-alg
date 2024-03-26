# 실전 10-6 팀 결성


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
    parent = [i for i in range(n+1)] # 0부터 n번까지

    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 0:
            union_parent(parent, a, b)
        else:
            if find_parent(parent, a) == find_parent(parent, b):
                print("YES")
            else:
                print("NO")
            
if __name__ == '__main__':
    solution()
