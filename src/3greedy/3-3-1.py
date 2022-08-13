# 예제 3-3 숫자 카드 게임

# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

# N x M 개의 숫자 카드 (N은 row, M은 column)
# 뽑고자 하는 카드가 포함된 row 선택
# 선택된 row에 포함된 카드 중 숫자가 가장 낮은 카드를 뽑아야 한다

# => 선택하는 row: 각 row의 최솟값 중 최댓값
# =======================================
# min 함수를 이용하는 방법
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 각 행의 최솟값 찾기
    min_data = min(data)
    # 최솟값 중 최댓값 찾기
    result = max(result, min_data)

print(result)
