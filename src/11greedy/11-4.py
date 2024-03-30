# 실전 11-4 만들 수 없는 금액


# =============
import sys


def solution():
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()

    target = 1
    for coin in coins:
        if target < coin:
            break
        target += coin

    print(target)

if __name__ == '__main__':
    solution()