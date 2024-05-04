# 실전 13-4 괄호 변환


# =============
def is_correct(p):
    cnt = 0 # (의 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            if cnt == 0: # ')' 개수가 더 많아진다면 올바르지 않은 문자열
                return False
            cnt -= 1
    return True

# 균형잡힌 문자열의 index 반환
def get_balanced_idx(p):
    cnt = 0 # (의 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0: # (, )의 개수가 같을 때 균형잡힌 문자열 idx가 끝나는 지점
            return i
def solution(p):
    answer = ''
    # 빈 문자열인 경우
    if p == '':
        return answer
    balanced_idx = get_balanced_idx(p)
    u = p[:balanced_idx + 1]
    v = p[balanced_idx + 1:]
    
    # u가 올바른 문자라면, v에 대하여 위와 동일한 작업 수행
    if is_correct(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # u의 첫번째와 마지막 문자 제거
        # 수정가능한 list 객체로 변환
        # 나머지 문자열(u)의 괄호 방향 뒤집어서 추가
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer