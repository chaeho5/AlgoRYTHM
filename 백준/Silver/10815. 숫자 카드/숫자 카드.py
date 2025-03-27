import sys
input = sys.stdin.readline

n = int(input())

card = list(map(int, input().split()))
card.sort()

m = int(input())
sang = list(map(int, input().split()))

def same_search(card, same):
    start = 0
    end = len(card) - 1

    while start <= end:
        mid = (start + end) // 2
        if card[mid] == same:
            return True
        elif card[mid] < same:
            start = mid + 1
        else:
            end = mid - 1
    return False

result = []

for num in sang:
    if same_search(card, num):
        result.append('1')
    else:
        result.append('0')

print(" ".join(map(str, result)))