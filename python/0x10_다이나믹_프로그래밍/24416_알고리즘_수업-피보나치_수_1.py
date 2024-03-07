N = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 1
dp_cnt = 0
for i in range(3, N+1):
    dp_cnt += 1
    dp[i] = dp[i-1] + dp[i-2]

print(fib(N), dp_cnt)


