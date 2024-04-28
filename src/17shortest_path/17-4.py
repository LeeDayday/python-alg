# 실전 17-4 숨바꼭질


# =============
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, n):
    queue = []
    min_distance = [INF for _ in range(n+1)] # 1번 헛간으로부터 최소 거리 저장
    min_distance[1] = 0 # 1번 헛간 거리 초기화

    # 1번 헛간과 인접한 헛간 heappush
    for node in graph[1]:
        heappush(queue, (1, node)) # (비용, 헛간 번호) 순으로 heappush
        min_distance[node] = 1
    while queue:
        curr_dist, curr_node = heappop(queue)
        # 최소 거리 갱신 여부 확인
        if curr_dist > min_distance[curr_node]:
            continue
        for new_node in graph[curr_node]:
            if curr_dist + 1 < min_distance[new_node]:
                min_distance[new_node] = curr_dist + 1
                heappush(queue, (curr_dist + 1, new_node))

    max_value = max(min_distance[1:-1])
    max_idx = min_distance.index(max_value)
    max_cnt = min_distance.count(max_value)

    print(max_idx, max_value, max_cnt)
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)] # 인접 리스트

    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    dijkstra(graph, n)
    