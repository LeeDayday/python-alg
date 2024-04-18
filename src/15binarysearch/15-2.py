# 실전 15-2 고정점 찾기


# =============
import sys
input = sys.stdin.readline

def binary_search(data, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == mid:
        return mid
    elif data[mid] > mid:
        return binary_search(data, 0, mid-1)
    else:
        return binary_search(data, mid + 1, end)


def solution(n, data):
    print(binary_search(data, 0, n - 1))

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    solution(n, data)