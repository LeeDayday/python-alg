# 실전 17-1 플로이드


# =============
import sys
input = sys.stdin.readline
INF = int(1e9)

def solution(graph, n):
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
                
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [[INF for _ in range(n)] for _ in range(n)]

    # 시작 도시와 도착 도시가 같은 경우는 없다
    for i in range(n):
        graph[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = min(graph[a-1][b-1], c)


    solution(graph, n)