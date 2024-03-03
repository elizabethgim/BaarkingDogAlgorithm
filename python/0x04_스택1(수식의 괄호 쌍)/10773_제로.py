import sys
input = sys.stdin.readline

# 80ms
K = int(input())

stack = []

for _ in range(K):
    N = int(input())

    if N == 0:
        stack.pop()
        continue

    stack.append(N)

print(sum(stack))

# 풀이2
# 92ms
K = int(input())
stack = []
total = 0

for _ in range(K):
    N = int(input())
    if N == 0:
        total -= stack.pop()
    else:
        total += N
        stack.append(N)

print(total)
