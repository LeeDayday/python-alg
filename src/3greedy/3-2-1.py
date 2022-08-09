# 예제 3-1 큰 수의 법칙

# N개의 자연수 (배열)
# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다

# =======================================

# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 자연수를 공백으로 구분하여 입력 받기
data = list(map(int,input().split()))

# 배열을 내림차순으로 정렬
data.sort(reverse=True)
first = data[0] # 가장 큰 수
second = data[1] # 그 다음으로 큰 수

result = 0

while True:
    for j in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 (총 m번 더했다면)
            break # 반복문 탈출
        m -= 1
        result += first
    if m == 0:
        break
    m -= 1
    result += second # 그 다음으로 큰 수 한 번 더하기

print(result)
