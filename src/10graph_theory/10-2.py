# 예제 10-2 개선된 서로소 집합 알고리즘 소스코드

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

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')