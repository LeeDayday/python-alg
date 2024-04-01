# 실전 12-2 문자열 재정렬


# =============
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    data = list(input().rstrip())
    data.sort()
    data = deque(data)

    cnt = 0
    while True:
        tmp = data.popleft()
        if '0' <= tmp and tmp <= '9':
            cnt += int(tmp)
        else:
            data.appendleft(tmp)
            break
    data.append(cnt)

    for i in data:
        print(i, end='')
if __name__ == '__main__':
    solution()