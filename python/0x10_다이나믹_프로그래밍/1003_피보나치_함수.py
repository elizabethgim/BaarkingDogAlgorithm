T = int(input())
dp = [0 for _ in range(41)]
dp[1] = 1

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(T):
    N = int(input())
    print(dp[N])

