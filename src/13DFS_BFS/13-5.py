# 실전 13-5 연산자 끼워넣기


# =============
import sys
from itertools import permutations
input = sys.stdin.readline


def solution(n, numbers, operations):
    min_result = int(1e9)
    max_result = -1 * int(1e9)
    for operation in operations:
        result = numbers[0]
        for op_idx in range(0, len(operation)):
            if operation[op_idx] == '+':
                result += numbers[op_idx + 1]
            elif operation[op_idx] == '-':
                result -= numbers[op_idx + 1]
            elif operation[op_idx] == 'x':
                result *= numbers[op_idx + 1]
            elif operation[op_idx] == '/':
                if result < 0:
                    result *= -1
                    result //= numbers[op_idx + 1]
                    result *= -1
                else:
                    result //= numbers[op_idx + 1]
                
        min_result = min(min_result, result)
        max_result = max(max_result, result)

    return max_result, min_result

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    cmds = list(map(int, input().split()))

    operations = ['+', '-', 'x', '/']
    ops = ''
    for i in range(len(cmds)):
        if cmds[i] != 0:
            ops += operations[i] * cmds[i]
    
    max_, min_ = solution(n, numbers, list(permutations(ops)))

    print(max_)
    print(min_)
