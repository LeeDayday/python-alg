
# =======================================
n, k = map(int, input().split())
result = 0

while True:
    # target: k의 배수 중 n과 가장 가까운 n 이하의 값
    # n이 k로 나누어 떨어질 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작다면(더 이상 나눌 수 없으면) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)