N = int(input())
arr = list(map(int, input().split()))
arr.sort()
time = [0 for _ in range(N)]
time[0] = arr[0]

for i in range(1, N):
    time[i] = time[i-1] + arr[i]

print(sum(time))
