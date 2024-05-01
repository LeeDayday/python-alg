# 실전 12-4 기둥과 보 설치


# =============
def is_possible_structure(answer):
    for x, y, a in answer:
        if a == 0: # 기둥 존재 조건
            # 바닥 위
            if y == 0:
                continue
            # 보 끝부분 위
            if [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            # 기둥 위
            if [x, y - 1, 0] in answer:
                continue
            return False
        else: # 보 존재 조건
            # 기둥 위
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
                continue
            # 보로 동시에 연결
            if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                continue
            return False
    return True
        
def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # a - 0: 기둥, 1: 보
        # b - 0: 삭제, 1: 설치
        if b == 0:
            # 삭제 후 존재 가능성 확인
            answer.remove([x, y, a])
            if not is_possible_structure(answer):
                # 다시 설치
                answer.append([x, y, a])
        else:
            # 설치 후 존재 가능성 확인
            answer.append([x, y, a])
            if not is_possible_structure(answer):
                # 다시 삭제
                answer.remove([x, y, a])
    return sorted(answer)
            