# 실전 14-1 국영수

# 국어 내림차순
# 영어 오름차순
# 수학 내림차순
# 이름 오름차순
# =============
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    data = []

    for _ in range(n):
        name, s1, s2, s3 = input().split()
        data.append([name, int(s1), int(s2), int(s3)])

    data.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

    for i in range(n):
        print(data[i][0])

if __name__ == '__main__':
    solution()