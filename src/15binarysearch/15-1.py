# 실전 15-1 정렬된 배열에서 특정 수의 개수 찾기


# =============
import sys
input = sys.stdin.readline

def binary_search(data, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if data[mid] == target:
        return 1 + binary_search(data, target, start, mid - 1) + binary_search(data, target, mid + 1, end)
    elif data[mid] > target:
        return binary_search(data, target, start, mid - 1)
    else:
        return binary_search(data, target, mid + 1, end)
def solution(n, x, data):
    
    cnt = binary_search(data, x, 0, n-1)

    if cnt == 0:
        return -1
    else:
        return cnt

if __name__ == '__main__':
    n, x = map(int, input().split())
    data = list(map(int, input().split()))
    print(solution(n, x, data))