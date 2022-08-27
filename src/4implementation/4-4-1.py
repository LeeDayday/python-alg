# 실전 4-4 게임 개발

# 게임 캐릭터가 맵 안에서 움직이는 시스템 개발
# 맵: N x M 크기
# 맵의 위치: (북쪽으로부터 떨어진 칸의 개수, 서쪽으로부터 떨어진 칸의 개수)
# 캐릭터는 상하좌우로 이동 가능, 바다 공간은 진입 x

# 교재 p.118 
# =======================================
# 교재 풀이

# N, M 입력
from winreg import DisableReflectionKey


n, m = map(int, input().split())
d = [[0] * m for _ in range(n)] # 세로 n, 가로 m인 직사각형 map 방문위치 저장 

# 초기 위치, 방향
x, y, dir = map(int, input().split()) 
d[x][y] = 1 # 현재 좌표 방문 처리

dx = [-1, 0, 1, 0] # 북 동 남 서 순으로
dy = [0, 1, 0, -1] # 북 동 남 서 순으로

# 전체 맵 정보 받기. 0:육지, 1: 바다
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3
    
# 시뮬레이션 시작
count = 1 # 초기 방문 수: 1
turn_time = 0
while True:
    turn_left()
    turn_time += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전 후 정면의 칸이 방문하지 않은 육지 칸이라면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 해당 칸 방문
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    
    # 더 이상 방문할 곳이 없다면 (한 바퀴 돌았다면)
    if turn_time == 4:
        # 바라보는 방향을 뒤로 한 채 한 칸 뒤로 돌아간다
        nx = x - dx[dir]
        ny = y - dy[dir]
        
        # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다
        if array[nx][ny] == 1:
            break
        else: # 뒤로 한 칸 갈 때, 해당 칸은 이미 방문을 했으므로 count 값을 올리지 않는다.
            d[nx][ny] = 1
            x, y = nx, ny
            turn_time = 0

print(count)
