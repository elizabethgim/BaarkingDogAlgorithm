N, M = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 0
total = 0
answer = 0

while start <= end:
    if total < M:
        if end == N:
            break
        total += num[end]
        end += 1
    else:
        if total == M:
            answer += 1

        total -= num[start]
        start += 1

print(answer)
