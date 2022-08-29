# 예제 5-2 큐

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제     
# =======================================
from collections import deque

# Queue를 구현하기 위해 deque library 사용
# deque: double-ended-queue. 양방향에서 데이터 처리 가능해 사용하기 편리함
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# 오른쪽으로 차곡 차곡 삽입
queue.popleft() 
# 가장 오래된 것(front 값)을 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 삽입한 순대로 출력
# deque([3, 7, 1, 4])
queue.reverse()
print(queue) # 나중에 들어온 순서로 출력
# deque([4, 1, 7, 3])