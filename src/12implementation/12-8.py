# 실전 12-8 외벽 점검



# =============
from itertools import permutations


def solution(n, weak, dist):
    # 원형 길이를 두배 늘려 일자 형태로 (시계, 반시계 모두 반영된 형태)
    len_ = len(weak) # 취약점 개수
    for i in range(len_):
        weak.append(weak[i]+n)
        
    answer = len(dist) + 1 # 최종 투입 친구 수, (최대 친구 수 + 1) 값으로 초기화 (점검 실패의 경우 고려)
    
    for start_idx in range(len_):
        # 친구를 나열할 수 있는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            friend_idx = 0
            # 해당 친구가 도달할 수 있는 마지막 위치
            position = weak[start_idx] + friends[friend_idx]
            # 시작점부터 모든 취약지점 확인
            for weak_idx in range(start_idx, start_idx + len_):
                # 다음 취약점 도달할 수 없는 경우, 친구 투입 추가
                if position < weak[weak_idx]:
                    friend_idx += 1
                    if friend_idx >= len(dist): # 더 투입할 수 없는 경우, 종료
                        break
                    # 해당 친구가 도달할 수 있는 마지막 위치 갱신
                    position = weak[weak_idx] + friends[friend_idx]
            answer = min(answer, friend_idx+1)
    if answer > len(dist): # answer이 갱신이 안된 경우 (모든 친구를 투입해도 불가능한 경우)
        answer = -1
            
    return answer