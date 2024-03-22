N = int(input())
arr = [0 for _ in range(N)]
arr[0] = 1

if N == 2:
    arr[1] = 2
elif N >= 3:
    arr[1] = 2
    for i in range(2, N):
        arr[i] = arr[i-1] + arr[i-2]

print(arr[-1] % 10007)
