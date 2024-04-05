# 실전 13-2 연구소


# =============
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def set_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                set_wall(cnt + 1)
                graph[i][j] = 0

def bfs():
    # 안전 영역 개수 반환
    global total
    tmp_graph = deepcopy(graph)
    tmp_queue = deepcopy(queue)    
    while tmp_queue:
        curr_i, curr_j = tmp_queue.popleft()
        for i in range(4):
            new_i = curr_i + dx[i]
            new_j = curr_j + dy[i]
            if new_i < 0 or new_i >= n:
                continue
            if new_j < 0 or new_j >= m:
                continue
            if tmp_graph[new_i][new_j] == 0:
                tmp_graph[new_i][new_j] = 2 # 감염 처리
                tmp_queue.append((new_i, new_j))

    # 안전 영역 (0) 개수 계산
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                cnt += 1
    
    total = max(total, cnt)


def solution():
    global graph, queue, n, m, total
    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    queue = deque()
    # 바이러스 위치 queue에 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j)) 
    
    # 3벽 세우기 모든 경우의 수를 고려
    total = 0
    set_wall(0)
    print(total)

            

if __name__ == '__main__':
    solution()