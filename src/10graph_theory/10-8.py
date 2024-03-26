# 예제 10-8 커리큘럼


# =============
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
INF = int(1e9)

def solution():
    n = int(input())
    costs = [0 for _ in range(n+1)] # 각 강의의 강의 시간
    indegree = [0 for _ in range(n+1)] # 각 강의의 진입차수
    graph = [[] for _ in range(n+1)] # 인접 리스트
    queue = deque()


    for i in range(1, n+1):
        data = list(map(int, input().split()))
        costs[i]= data[0] # 각 강의의 강의 시간
        for node in data[1:]:
            if node == -1:
                if indegree[i] == 0:
                    queue.append(i) # 진입차수가 0인 정점 queue에 추가
            else:
                indegree[i] += 1
                graph[node].append(i) # 인접 리스트 추가

    result = deepcopy(costs) # 최종 결과      
      
    while queue:
        curr_node = queue.popleft()
        for new_node in graph[curr_node]:
            indegree[new_node] -= 1
            result[new_node] = max(result[new_node], result[curr_node] + costs[new_node])
            if indegree[new_node] == 0:
                queue.append(new_node)

    for i in range(1, n+1):
        print(result[i])


if __name__ == '__main__':
    solution()