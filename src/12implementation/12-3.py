# 실전 12-3 문자열 압축


# =============
import sys
input = sys.stdin.readline

def solution(s):
    answer = len(s)
    n = len(s)
    # 문자열을 i개 단위로 자르기 (1개 ~ n/2)
    for i in range(1, n // 2 + 1):
        tmp = s[:i]
        cnt = 1    
        result = ''
        for j in range(i, n, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                result += str(cnt) + tmp if cnt >=2 else tmp
                tmp = s[j:j+i]
                cnt = 1
        # 마지막 단어까지 추가
        result += str(cnt) + tmp if cnt >= 2 else tmp
        answer = min(answer, len(result))
                
    return answer

if __name__ == '__main__':
    s = input().rstrip()
    print(solution(s))