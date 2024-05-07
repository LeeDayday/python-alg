# 실전 13-5 연산자 끼워넣기


# =============
import sys
from itertools import permutations
input = sys.stdin.readline

def dfs(i, now, numbers, n):
    global min_result, max_result, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_result = min(min_result, now)
        max_result = max(max_result, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + numbers[i], numbers, n)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - numbers[i], numbers, n)
        if mul > 0:
            mul -= 1
            dfs(i+1, now * numbers[i], numbers, n)
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/numbers[i]), numbers, n)
            div += 1

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())

    min_result = int(1e9)
    max_result = -int(1e9)

    dfs(1, numbers[0], numbers, n)

    print(max_result)
    print(min_result)
