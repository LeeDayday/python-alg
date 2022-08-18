# 예제 4-1 상하좌우

# N x N 크기의 정사각형, 공간읜 1 x 1 크기로 나누어져 있으
# 가장 왼쪽 위는 (1,1), 가장 오른쪽 아래는 (N, N)
# 시작 좌표는 (1,1)
# L, R, U, D 로 이루어진 이동 계획서. 최종 지점의 좌표를 출력
# 단, 공간을 벗어나는 움직임은 무시한다

# =======================================
# 내 풀이
n = int(input())
x, y = 1, 1
moves = list(input().split())

for move in moves: 
    if move == 'L':
        if x - 1 > 0:
            x -= 1
    elif move == 'R':
        if x + 1 < n:
            x += 1
    elif move == 'U':
        if y - 1 > 0:
            y =- 1
    elif move == 'D':
        if y + 1 < n:
            y += 1
    print(y, x)

print(y, x)