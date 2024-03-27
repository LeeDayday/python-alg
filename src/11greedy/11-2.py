# 실전 11-2 곱하기 혹은 더하기


# =============
import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    total = int(s[0])
    for i in range(1, len(s)):
        total = max(total + int(s[i]), total * int(s[i]))
    print(total)


if __name__ == '__main__':
    solution()