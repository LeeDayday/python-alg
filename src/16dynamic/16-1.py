# 실전 16-1 금광

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
"""

# =============
import sys


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())

        data = list(map(int, input().split()))

        graph = []
        
        idx = 0
        for _ in range(n):
            graph.append(data[idx:idx+m])
            idx += m
        
        # 1번째 column부터 순서대로
        for j in range(1, m):
            for i in range(n):
                # 왼쪽 위에서 오는 경우
                if i == 0: # 0번째 row는 '왼쪽 위' 경우가 존재하지 않음
                    left_up = 0
                else:
                    left_up = graph[i-1][j-1]

                # 왼쪽에서 오는 경우
                left = graph[i][j-1] # '왼쪽' 경우는 항상 존재

                # 왼쪽 아래에서 오는 경우
                if i == n - 1: # 마지막 row는 '왼쪽 아래' 경우가 존재하지 않음
                    left_down = 0
                else:
                    left_down = graph[i+1][j-1]
                
                graph[i][j] = graph[i][j] + max(left_up, left, left_down)
    
        # 마지막 row의 최댓값 구하기
        max_result = 0
        for i in range(n):
            max_result = max(max_result, graph[i][-1])
        
        print(max_result)
        