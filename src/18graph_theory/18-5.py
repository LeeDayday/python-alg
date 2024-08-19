# 실전 18-5 최종 순위


# =============
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) # 팀 개수
    indegree = [0 for _ in range(n+1)] # 진입 차수
    graph = [[False for _ in range(n+1)] for _ in range(n+1)] # 인접 행렬
    last_year = list(map(int, input().split()))
    # 자기보다 낮은 등수를 모두 가리킴
    for i in range(n):
        for j in range(i+1, n):
            graph[last_year[i]][last_year[j]] = True
            indegree[last_year[j]] += 1

    # 올해 변경된 순위
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split()) # 올해는 팀 a 순위가 팀 b 순위보다 높다
        # 간선 방향, 진입 차수 수정하기
        if graph[a][b]:
            # 간선 방향 뒤집기
            graph[a][b] = False
            graph[b][a] = True
            # 진입 차수 수정
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬
    result = []
    queue = deque()

    # 진입 차수가 0인 정점을 queue에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    unique = True # 위상 정렬 결과가 유일한지의 여부
    cycle = False # 사이클 발생 여부

    # 정확히 노드의 개수만큼 반복 (만족 안할 시, 사이클 발생)
    for i in range(n):
        # queue가 빈 경우, 사이클 발생
        if len(queue) == 0:
            cycle = True
            break
        # queue가 2개 이상인 경우, 결과 유일성 위반
        if len(queue) >= 2:
            unique = False
            break
        node = queue.popleft()
        result.append(node)
        # 해당 노드와 연결된 노드들의 진입차수 변경
        for j in range(1, n+1):
            if graph[node][j]:
                indegree[j] -= 1
                # 새롭게 진입차수 0인 정점 queue에 삽입
                if indegree[j] == 0:
                    queue.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not unique:
        print("?")
    else:
        print(*result)
