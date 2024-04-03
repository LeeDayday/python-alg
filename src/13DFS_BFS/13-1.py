# 실전 13-1 특정 거리의 됫 찾기


# =============
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(graph, n, dist_goal, start):
    q = []
    dist = [INF] * (n+1)

    # 시작 노드
    heappush(q, (0, start))
    dist[start] = 0

    while q:
        curr_dist, curr_node = heappop(q)
        # curr_node의 인접 노드를 보며 시작 노드로부터의 최단 거리 업데이트
        for n_node in graph[curr_node]:
            # n_node에 대해 갱신이 필요한 경우
            if dist[n_node] > curr_dist + 1:                
                dist[n_node] = curr_dist + 1
                heappush(q, (curr_dist + 1, n_node))
    cnt = 0
    for i in range(1, n+1):
        if dist[i] == dist_goal:
            cnt += 1
            print(i)

    if cnt == 0:
        print(-1)

def solution():
    n, m, k, x = map(int, input().split())
    graph = [[]for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)

    dijkstra(graph, n, k, x)
if __name__ == '__main__':
    solution()