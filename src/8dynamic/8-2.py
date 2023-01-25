# 실전 8-2 1로 만들기


# 5로 나누어 떨어지면 5로 나눈다
# 3으로 나누어 떨어지면 3으로 나눈다
# 2로 나누어 떨어지면 2로 나눈다
# 1을 뺀다
# 최소한의 연산으로 1을 만들어라
# =============
n = int(input())

dp = [0] * 30001

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)

print(dp[n])