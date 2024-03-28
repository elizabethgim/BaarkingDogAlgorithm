import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
dp[1] = numbers[1]

for i in range(2, N+1):
    dp[i] = dp[i-1]+numbers[i]

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[end] - dp[start-1])
