# 실전 16-6 편집 거리


# =============
import sys
input = sys.stdin.readline

def solution(a, b):
    len_a = len(a)
    len_b = len(b)

    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    for i in range(1, len_a + 1):
        dp[i][0] = i
    for i in range(1, len_b + 1):
        dp[0][i] = i

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            #문자가 같은 경우, 이전 단계 수 그대로 대입
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 삽입/삭제/교환 중 최소 비용 찾아 대입
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[-1][-1]

a = input().rstrip()
b = input().rstrip()

print(solution(a, b))
