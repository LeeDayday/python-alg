# 실전 15-3 공유기 설치


# =============
import sys
input = sys.stdin.readline

def solution(data, n, c):
    data.sort()
    # gap을 기준으로 이진 탐색 수행
    start = data[1] - data[0] # 최소 gap
    end = data[-1] - data[0] # 최대 gap
    result = 0
    while start <= end:
        mid = (start + end) // 2
        value = data[0]
        cnt = 1 # 첫번째 집 (idx: 0) 에 공유기 설치
        for i in range(1, n): # 첫번째 집에서부터 mid 거리 만큼 공유기 설치
            if data[i] >= value + mid:
                value = data[i]
                cnt += 1
        if cnt >= c: # 공유기를 설치할 수 있는 경우, 거리를 증가
           start = mid + 1
           result = mid # 최적의 결과를 저장
        else:
           end = mid - 1
    print(result)
          
        
if __name__ == '__main__':
    n, c = map(int, input().split())
    data = [] # 집의 위치
    for _ in range(n):
        data.append(int(input()))

    solution(data, n, c)
