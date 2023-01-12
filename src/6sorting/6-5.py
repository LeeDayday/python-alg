# 예제 6-4 파이썬의 장점을 살린 퀵 정렬

     
# =======================================
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

print(count)

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
