# 실전 11-3 문자열 뒤집기


# =============
import sys
input = sys.stdin.readline


def solution():
    s = input().rstrip()
    cnt = [0, 0]
    tmp = int(s[0])
    # 숫자 덩어리 count
    for i in range(1, len(s)):
        if tmp != int(s[i]):
            cnt[tmp] += 1
            tmp = int(s[i])
    # 마지막 숫자 덩어리까지 더하기
    cnt[tmp] += 1

    print(min(cnt))
if __name__ == '__main__':
    solution()
