# 예제 4-2 시각

# 정수 N(0<=23)이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수

# =======================================
# 내 풀이 -> 여사건으로 접근
# 전체 경우에서 3이 포함되지 않은 경우를 뺀다

n = int(input())
cnt = 0

# 00~59 사이에 3이 포함된 경우 (min, sec)
for i in range(0,60):
    if i == 3:
        print(i)
        cnt += 1
    elif i // 10 == 3 or i % 10 == 3:
        print(i)
        cnt += 1

non_cnt = 60 - cnt # 여사건
print("non_sec_cnt:",non_cnt)

# 00~23시에 3이 포함된 경우 (hour)
cnt = 0
for i in range(0,n+1):
    if i == 3:
        print(i)
        cnt += 1
    elif i // 10 == 3 or i % 10 == 3:
        print(i)
        cnt += 1

non_hour_cnt = n + 1 - cnt # 여사건
print("non_hour_cnt:",non_hour_cnt)

total = (n + 1) * 60 * 60 # 전체 경우의 수
result = total - non_cnt * non_cnt * non_hour_cnt

print(result)