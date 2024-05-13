# 실전 16-2 정수 삼각형



# =============
import sys
input = sys.stdin.readline

def solution(triangle, n):
    for i in range(1, n):
        for j in range(0, i+1):
            if j - 1 < 0: # 왼쪽 위 대각선이 존재하지 않는 경우
                triangle[i][j] += triangle[i-1][j]
            elif i - 1 < j: # 오른쪽 위 대각선이 존재하지 않는 경우
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1]) # 마지막 행의 최댓값 반환

    
    
    

if __name__ == '__main__':
    n = int(input())
    triangle = []

    for _ in range(n):
        triangle.append(list(map(int, input().split())))
    
    print(solution(triangle, n))