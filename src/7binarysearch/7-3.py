# 7-3 반복문으로 구현한 이진 탐색 소스 코드

# =======================================
def binary_search(start, end, target, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(0, n - 1, target, array)
if result == None:
    print('No such target')
else:
    print(result + 1)