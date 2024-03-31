# 실전 11-4 럭키 스트레이트


# =============
import sys
input = sys.stdin.readline

def solution():
    data = input().rstrip()
    tmp = len(data) // 2
    sum_a = 0
    sum_b = 0
    for num in data[:tmp]:
        sum_a += int(num)
    for num in data[tmp:]:
        sum_b += int(num)

    if sum_a == sum_b:
        print("LUCKY")
    else:
        print("READY")

if __name__ == '__main__':
    solution()