# 7-5 떡볶이 떡 만들기

# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M 만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
# =======================================
n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)
# 조건을 만족하는 start까지의 길이가 높이의 최댓값
result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 떡 자르기
        if x > mid:
            total += x - mid # 잘린 떡의 길이
    if total < m: # 원하는 값보다 적으면 높이를 줄여야 함
        end = mid - 1
    else: # 적어도 m은 만족, 높이 최댓값이 목적
        result = mid
        start = mid + 1
    print("i'm in while %d %d",(start, end))

print(result)
