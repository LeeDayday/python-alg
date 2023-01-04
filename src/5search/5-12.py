# 실전 5-12 미로 탈출

# N x M 크기의 미로
# 초기 위치: (1, 1), 탈출구: (N, M)
# 한 번에 한 칸씩 이동
# 0: 이동 불가, 1: 이동 가능
# 최소 칸의 개수 구하기
# =======================================
# 2차원 배열에서의 탐색 문제를 그래프 형태로 생각하여 풀이
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
            x, y = queue.popleft()
            # 다음 위치 결정
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 밖인 경우
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                # 접근 불가 지역인 경우
                if graph[nx][ny] == 0:
                    continue
                # 방문 가능한 노드 방문
                if graph[nx][ny] == 1:
                    # 초기 위치로부터 방문한 노드 개수 저장
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    return graph[n-1][m-1]
    

print(BFS(0, 0))