# 실전 17-2 정확한 순위


# =============
import sys
input = sys.stdin.readline
INF = int(1e9)

def solution(data, n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                data[j][k] = min(data[j][k], data[j][i] + data[i][k])

    result = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if data[i][j] != INF or data[j][i] != INF:
                cnt += 1
            if cnt == n: # 자기 자신까지 돌 수 있는 경우
                result += 1
    print(result)
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        data[i][i] = 0 # 자기자신으로 가는 비용은 0 처리 (도달 가능하다고 가정)

    for _ in range(m):
        a, b = map(int, input().split()) # a의 점수 < b의 점수
        data[a][b] = 1

    solution(data, n)
