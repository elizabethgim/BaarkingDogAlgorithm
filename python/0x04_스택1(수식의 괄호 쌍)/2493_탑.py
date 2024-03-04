N = int(input())
towers = list(map(int, input().split()))
lazer = [0 for _ in range(N)]
stack = []

for i in range(N):
    while stack:
        if towers[stack[-1][0]] < towers[i]:
            stack.pop()
        else:
            lazer[i] = stack[-1][0] + 1
            break

    stack.append((i, towers[i]))

print(*lazer)
