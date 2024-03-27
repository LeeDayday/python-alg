# 실전 11-1 모험가 길드


# =============
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    cnt = 0
    idx = 0
    
    while True:
        idx += num_list[idx]
        if idx < n:
            cnt += 1
        else: 
            break
    
    print(cnt)
        
if __name__ == '__main__':
    solution()