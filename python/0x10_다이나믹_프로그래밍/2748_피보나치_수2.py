N = int(input())
fibonacci = [0 for _ in range(N+1)]
fibonacci[1] = 1
if N < 2:
    print(1)
else:
    fibonacci[2] = 1
    if N > 2:
        for i in range(3, N+1):
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

    print(fibonacci[N])
