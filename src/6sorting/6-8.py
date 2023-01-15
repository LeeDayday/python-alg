# 실전 6-8 두 배열의 원소 교체

     
# =======================================
# 결론: A의 최솟값과 B의 최댓값 swap

n, k = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)

for i in range(k):
    if listA[i] < listB[i]:
        listA[i], listB[i] = listB[i], listA[i]
    else:
        break

print(sum(listA))