# 실전 12-5 뱀


# =============
import sys
from collections import deque
input = sys.stdin.readline


# n x n 크기의 보드
n = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

# k개의 사과 위치 입력
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    graph[i][j] = 1

# l개의 뱀 방향 변환 정보
l = int(input())
pos = dict()
for _ in range(l):
    x, c = input().split()
    pos[int(x)] = c

# 뱀의 위치 정보, front: 뱀 머리, rear: 뱀 꼬리
snake = deque()
snake.append((1, 1))
# 오른쪽, 아래, 왼쪽, 위 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 뱀의 머리 방향
idx = 0
total_time = 0
while True:
    # 전진
    total_time += 1

    curr_x, curr_y = snake[0]

    new_x = curr_x + dx[idx]
    new_y = curr_y + dy[idx]

    # 보드 크기를 벗어난 경우 게임 종료
    if new_x <= 0 or new_y <= 0 or new_x > n or new_y > n:
        break
    # 이미 뱀이 있는 경우
    if graph[new_x][new_y] == 2:
        break
    # 이동 가능한 경우 뱀 위치, 보드판 업데이트
    snake.appendleft((new_x, new_y)) # 뱀 머리 이동
    if graph[new_x][new_y] == 0: # 사과가 없는 경우
        tail_x, tail_y = snake.pop() # 뱀 꼬리 이동
        graph[tail_x][tail_y] = 0        
        
    graph[new_x][new_y] = 2 # 보드 업데이트

    # 뱀 머리 방향 업데이트
    if total_time in pos:
        if pos[total_time] == 'L':
            idx = (idx - 1) % 4
        else:
            idx = (idx + 1) % 4

         
print(total_time)