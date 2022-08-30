# 예제 5-5 팩토리얼
# 2가지 방식으로 구현
# =======================================

# 반복문으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀함수로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))
print(factorial_iterative(5))