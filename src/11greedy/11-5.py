# 실전 11-5 볼링공 고르기


# =============
import sys
input = sys.stdin.readline

def solution():
    n, _ = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()

    total = 0
    for i in range(n - 1):
        tmp = 1
        while data[i] == data[i+tmp]:
            tmp += 1
            if i + tmp == n:
                break
        total += n - (i + tmp)
    print(total)


if __name__ == '__main__':
    solution()