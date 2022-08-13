# 2중 반복문을 이용한 풀이
# =======================================

n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 각 행의 최솟값 찾기
    min_value = 10001
    for value in data:
        if min_value > value:
            min_value = value
    result = max(min_value, result)

print(result)