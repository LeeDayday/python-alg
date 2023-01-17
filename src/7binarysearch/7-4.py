# 7-4 부품 찾기

# =======================================

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if(array[mid] == target):
        return mid
    elif (array[mid] < target):
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)
    

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
customer_array = list(map(int, input().split()))

for i in customer_array:
    result = binary_search(array, i, 0, n - 1)
    if result == None:
        print('No', end=' ')
    else:
        print('Yes', end=' ')

