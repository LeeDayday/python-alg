# 실전 17-3 화성 탐사


# =============
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dijkstra(graph, n):
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = graph[0][0]
    queue = []
    heappush(queue, (distance[0][0], 0, 0)) # distance, x좌표, y좌표
    while queue:
        curr_dist, curr_x, curr_y = heappop(queue)
        
        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
                continue
            tmp_distance = curr_dist + graph[new_x][new_y]
            if tmp_distance < distance[new_x][new_y]:
                heappush(queue, (tmp_distance, new_x, new_y))
                distance[new_x][new_y] = tmp_distance

    print(distance[-1][-1])

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))

        dijkstra(graph, n)