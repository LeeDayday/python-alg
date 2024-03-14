# 실전 9-1 미래 도시


# =============
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, n, start):
    q = [] # 우선순위 큐
    distance = [INF] * (n+1) # 시작노드로부터 최단 거리

    # 시작 노드 처리
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        curr_weight, curr_node = heappop(q)
        # distance를 갱신할 필요가 있는지 검사
        print(curr_node)
        if curr_weight > distance[curr_node]:
            continue
        # distance 갱신
        for n_node in graph[curr_node]:
            # start -> n_node vs start -> curr_node -> n_node
            cost = curr_weight + n_node[1]
            if distance[n_node[0]] > cost:
                distance[n_node[0]] = cost
                heappush(q, (cost, n_node[0]))
    
    print(distance)
    # 총 도시 개수, 걸리는 시간 구하기
    total = 0
    max_time = 0
    for i in range(1, n+1):
        if distance[i] != INF and distance[i] != 0:
            total += 1
            max_time = max(max_time, distance[i])

    print(total, max_time)        


def solution():
    n, m, c = map(int, input().split())
    graph = [[]for _ in range(n+1)]

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra(graph, n, c)
if __name__ == '__main__':
    solution()