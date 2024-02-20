N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])

'''
N = int(input())

answer = int(1e6)


def dp(X, cnt):
    global answer
    print(X)
    if X == 0:
        answer = min(answer, cnt)
        return

    elif X % 3 == 0:
        dp(X//3, cnt+1)
    elif X % 2 == 0:
        dp(X//2, cnt+1)
    else:
        dp(X-1, cnt+1)

dp(N, 0)

print(answer)
'''