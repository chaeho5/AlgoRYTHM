import sys
import heapq
input = sys.stdin.readline

n = int(input())

deck = []
for _ in range(n):
    num = int(input())
    deck.append(num)

heapq.heapify(deck)

result = 0

while len(deck)  > 1:
    f_deck = heapq.heappop(deck)
    s_deck = heapq.heappop(deck)

    hop = f_deck + s_deck
    result += hop

    heapq.heappush(deck, hop)
print(result)