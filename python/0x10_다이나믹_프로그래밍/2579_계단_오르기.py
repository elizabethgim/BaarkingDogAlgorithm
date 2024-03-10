'''
52ms
31120KB
'''

N = int(input())

stair = [0]

for _ in range(N):
    stair.append(int(input()))

dp = [0 for _ in range(N+1)]

dp[1] = stair[1]

if N > 1:
    dp[2] = stair[1]+stair[2]

if N > 2:
    dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

if N > 3:
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2]+stair[i])

print(dp[N])


'''
4
10
20
15
25


1, 3
10+15 = 45

1, 3, 4
10+15+25 = 50

1, 2, 4
10+20+25 = 55

1, 3, 4, 5
10+15+25+10 = 60

1, 2, 4, 5
10+20+25+10 = 65

1, 3, 4, 5
10+15+25+20 = 70

1, 2, 4, 5 
10+20+25+20 = 75
'''