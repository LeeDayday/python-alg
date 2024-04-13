# 실전 14-2 실패율


# =============
def solution(N, stages):
    answer = []
    result = [0 for _ in range(N)]
    
    stages.sort()
    
    for i in range(len(stages)): # result에 스테이지 번호 별 cnt 저장
        if stages[i] == N + 1:
            continue
        result[stages[i]-1] += 1 
    
    approached_people = len(stages) # 스테이지에 도달한 플레이어 수
    for i in range(len(result)): # answer에 (실패율, 스테이지 번호) 저장
        if approached_people == 0:
            answer.append((0, i + 1))
        else:
            answer.append((result[i] / approached_people, i + 1))
        approached_people -= result[i]

    # cnt 기준 내림차순 > 스테이지 번호 기준 오름차순
    answer.sort(key=lambda x: (-x[0], x[1]))
    
    # answer에 스테이지 번호만 저장
    for i in range(len(answer)):
        answer[i] = answer[i][1]

    return answer