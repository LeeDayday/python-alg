# 실전 14-2 안테나


# =============
import sys
input = sys.stdin.readline


def solution(n, data):
    print(data[(n-1) // 2])

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    solution(n, data)