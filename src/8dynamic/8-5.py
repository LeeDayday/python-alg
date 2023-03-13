# 실전 8-5 효율적인 화폐 구성


# N 가지 종류의 화폐
# 화폐들의 개수를 최소한으로 이용해서 M원이 되도록
# 최소한의 화폐 개수 출력, 불가능할 때는 -1 출력
# =============

N, M = map(int, input().split())

money = []
for i in range(N):
    money.append(int(input()))

dp = [10001] * (M + 1)

dp[0] = 0
for i in range(N):
    for j in range(money[i], M+1):
        if j % money[i] == 0:
            if dp[j - money[i]] != 10001:
                dp[j] = min(dp[j], dp[j-money[i]]+1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])