# 더 멋지게 푸는 방법...✨
# 문제 결론: 수열 (first * k번 + second * 1번) 최대한 많이 더하기

# 수열의 길이: (first*k번 + second*1번) => k+1
# 수열이 반복되는 횟수: m // (k+1)
# 나머지 더해줘야 하는 값: first * (m % (k + 1))

# =======================================

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수
count = m//(k+1)*k + m%(k+1)

result = 0
result += first * count
result += second * (m - count)

print(result)

