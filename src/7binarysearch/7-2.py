# 7-2 재귀함수로 구현한 이진 탐색 소스 코드

# =======================================

def binary_search(start, end, target, array):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(mid + 1, end, target, array)
    else:
        return binary_search(start, mid - 1, target, array)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(0, n - 1, target, array)
if result == None:
    print('No such target')
else:
    print(result + 1)