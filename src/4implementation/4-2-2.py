# =======================================
# 교재 풀이 -> 완전 탐색 유형
# 모든 경우의 수가 86,400가지 밖에 존재하지 않기 때문에
# 3중 반복문을 이용해도 시간 제한 초과 x

# 탐색해야 할 전체 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면 적절하다

# H 입력받기
h = int(input())

count = 0
for i in range(h+1): # hour
    for j in range(60): # min
        for k in range(60): #sec
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)