# 실전 14-4 카드 정렬하기


# =============
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solution(cards):
    total = 0
    while len(cards) != 1:
        card1 = heappop(cards)
        card2 = heappop(cards)
        total += card1 + card2
        heappush(cards, card1 + card2)
    return total


if __name__ == '__main__':
    n = int(input())
    cards = []
    for _ in range(n):
        heappush(cards, int(input()))
    print(solution(cards))