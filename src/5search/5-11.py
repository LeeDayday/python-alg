# 실전 5-11 음료수 얼려 먹기

# N x M 크기의 얼음 틀
# 뚫려 있는 부분: 0, 칸막이가 존재하는 부분: 1
# 1로 둘러싸인 0 집합 개수 => 아이스크림 개수
# =======================================
# 2차원 배열에서의 탐색 문제를 그래프 형태로 생각하여 풀이

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))




# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def DFS(x, y):
    # print("x, y: ",x, y)
    # 얼음틀 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문하지 않은 노드(+구멍이 뚫려 있는 부분)라면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 후
        graph[x][y] = 1
        # 상하좌우 dfs 실행
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True
    # 이미 방문한 노드라면 False 반환
    return False
    
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if DFS(i, j) == True:
            result += 1

print(result)
    


