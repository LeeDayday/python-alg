# 실전 16-5 못생긴 수



# =============
import sys
input = sys.stdin.readline

# 못생긴 수를 작은 수부터 차례대로 확인
def solution(n):
    dp = [0] * n
    dp[0] = 1

    idx_2 = idx_3 = idx_5 = 0
    next_2, next_3, next_5 = 2, 3, 5

    for i in range(1, n):
        dp[i] = min(next_2, next_3, next_5)
        if dp[i] == next_2:
            idx_2 += 1
            next_2 = dp[idx_2] * 2
        if dp[i] == next_3:
            idx_3 += 1
            next_3 = dp[idx_3] * 3
        if dp[i] == next_5:
            idx_5 += 1
            next_5 = dp[idx_5] * 5

    return dp[n-1]    


        

n = int(input())
print(solution(n))