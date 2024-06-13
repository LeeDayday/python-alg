# 실전 16-3 퇴사



# =============
import sys

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0] * (n + 1) # 해당 index까지 최대 이익 저장

max_value = 0
for i in range(n - 1, -1, -1):
    time = data[i][0] + i
    if time > n: # 퇴사 이후 상담이 끝나지 않는 경우
        dp[i] = max_value
    else:
        dp[i] = max(data[i][1] + dp[time], max_value)
        max_value = dp[i]

print(max_value)
