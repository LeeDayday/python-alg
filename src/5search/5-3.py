# 예제 5-3 재귀함수
# 오류 - 재귀의 최대 깊이를 초과
# =======================================
def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded in comparison