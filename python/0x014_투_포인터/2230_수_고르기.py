N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
arr.sort()
left, right = 0, 0
answer = 2e9
while left < N and right < N:
    diff = abs(arr[left]-arr[right])

    if diff < M:
        right += 1
    else:
        answer = min(answer, diff)
        left += 1
print(answer)
