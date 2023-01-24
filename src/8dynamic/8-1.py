# 예제 8-1. Fibonacci - Memoization
d = [0] * 100

def fibo(x):
    if x <=2:
        return 1
    # 이미 계산한 적이 있다면
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(6))