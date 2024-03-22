# 예제 10-3 서로소 집합을 이용한 사이클 판별 소스코드

# 전체 집합: {1, 2, 3, 4, 5, 6}
# 합집합 연산 이후:{1, 2, 3, 4}, {5, 6}

# O(V + M(1+log(2-M/V)V))
# =============
def find_parent(parent, x):
    # 경로 압축 적용. parent는 곧 root를 가리킴
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블

# 부모 테이블 초기화 (각 노드의 부모를 자기 자신으로)
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        print(f"{a}, {b} cycle")
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 O")
else:
    print("사이클 X")