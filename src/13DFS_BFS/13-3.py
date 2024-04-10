# 실전 13-3 경쟁적 전염


# =============
import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, virus_q, s, n):
    for _ in range(s):
        tmp_virus_q = []
        while virus_q:
            v, v_x, v_y = heappop(virus_q)
            for i in range(4):
                new_x = v_x + dx[i]
                new_y = v_y + dy[i]
                if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
                    continue
                if graph[new_x][new_y] != 0:
                    continue
                graph[new_x][new_y] = v
                heappush(tmp_virus_q, (v, new_x, new_y))
        virus_q = tmp_virus_q


def solution():
    n, _ = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    s, x, y = map(int, input().split())

    virus_q = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                heappush(virus_q, (graph[i][j], i, j)) # (바이러스 종류, (좌표)) 우선순위 큐에 저장
    
    bfs(graph, virus_q, s, n)

    print(graph[x-1][y-1])

if __name__ == '__main__':
    solution()