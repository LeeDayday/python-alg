# 실전 6-6 위에서 아래로

# 수열을 내림차순으로 정렬하는 프로그램
# =======================================
n = int(input())

array=[]

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

print(array)