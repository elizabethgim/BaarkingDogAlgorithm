K = int(input())
stack = []
total = 0
for _ in range(K):
    N = int(input())
    if N != 0:
        stack.append(N)
        total += N
    else:
        x = stack.pop()
        total -= x

print(total)

