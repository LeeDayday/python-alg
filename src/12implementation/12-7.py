# 실전 12-7 치킨 배달


# =============
from itertools import combinations
import sys
input = sys.stdin.readline


def solution(house, chicken_candidates):
    # 치킨집 각 조합에 대하여 최소 치킨거리 구하기
    result = int(1e9)
    for candidate in chicken_candidates:
        candidate_result = 0
        for h_x, h_y in house:
            tmp = int(1e9)
            for c_x, c_y in candidate:
                tmp = min(tmp, abs(h_x - c_x) + abs(h_y - c_y))
            candidate_result += tmp
        result = min(result, candidate_result)
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    house, chicken = [], [] # 집, 치킨집 좌표 관리

    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(n):
            if data[j] == 1:
                house.append((i, j))
            if data[j] == 2:
                chicken.append((i, j))

    # m개의 치킨집 조합
    chicken_candidates = list(combinations(chicken, m))
    print(solution(house, chicken_candidates))