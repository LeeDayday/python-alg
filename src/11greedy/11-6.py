# 실전 11-6 무지의 먹방 라이브


# =============
import heapq

def solution(food_times, k):
    answer = 0
    cnt = len(food_times) # 음식 종류 수
    # 모든 음식을 다 먹는 경우
    if sum(food_times) <= k:
        answer = -1
    else:
        # 섭취 소요 시간이 적은 음식부터 다 먹으므로, 우선순위 큐로 관리
        q = []
        for i in range(cnt):
            heapq.heappush(q, (food_times[i], i + 1)) # (소요 시간, 음식 번호)
            
        # 최대한 음식 종류 줄이기 (heappop 수행)
        total_time = 0 # 현재까지 소요된 시간
        previous_time = 0 # 마지막으로 다 먹은 음식의 소요 시간
        while total_time + ((q[0][0] - previous_time) * cnt) <= k:
            curr_time, _ = heapq.heappop(q)
            total_time += (curr_time - previous_time) * cnt
            cnt -= 1
            previous_time = curr_time
        
        # heapq를 음식 번호 기준으로 정렬
        result = sorted(q, key=lambda x:x[1])
        answer = result[(k - total_time) % cnt][1]
        
    return answer