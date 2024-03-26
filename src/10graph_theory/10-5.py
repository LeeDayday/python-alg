# 예제 10-5 위상 정렬 알고리즘

# O(V+E)
# =============
from collections import deque

# 노드의 개수, 간선의 개수 입력
v, e = map(int, input().split())

# 진입 차수 리스트 초기화
indegree = [0 for _ in range(v+1)] 

# 인접 리스트 초기화
graph = [[] for _ in range(v+1)]

for _ in range(e):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

# 위상 정렬 함수
def topology_sort():
    queue = deque()
    result = []
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        curr_node = queue.popleft()
        result.append(curr_node)
        for new_node in graph[curr_node]:
            indegree[new_node] -= 1
            if indegree[new_node] == 0:
                queue.append(new_node)
    
    return result

print(topology_sort())