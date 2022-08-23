# 실전 4-3 왕실의 나이트

# 8 x 8 좌표 평면
# 행 위치: 1~8, 열 위치: a~h
# 특정한 한 칸에 나이트가 서 있다
# 나이트는 L자 형태로만 이동할 수 있으며, 정원 밖으론 x

# 초기 위치에서 나이트가 이동할 수 있는 경우의 수 출력
# =======================================
# 내 풀이
knight = input()
row = int(knight[1]) # knight[1]은 string. int로 형변환
col = int(ord(knight[0]) - ord('a')) + 1 # ord는 문자를 아스키 코드로 변환하는 함수
# row, col은 모두 정수형

move_up = row - 2
move_down = row + 2
move_left = col - 2
move_right = col + 2

print("u,d,l,r:", move_up,move_down,move_left,move_right)
# 이동할 수 있는 경우의 수
cnt = 0
if move_up >= 1:
    if move_left >= 1:
        cnt += 1
    if move_right <= 8:
        cnt += 1
if move_down <= 8:
    if move_left >= 1:
        cnt += 1
    if move_right <= 8:
        cnt += 1
if move_left >= 1:
    if move_up >= 2:
        cnt += 1
    if move_down <= 8:
        cnt += 1
if move_right >= 1:
    if move_up >= 2:
        cnt += 1
    if move_down <= 8:
        cnt += 1
print(cnt)
