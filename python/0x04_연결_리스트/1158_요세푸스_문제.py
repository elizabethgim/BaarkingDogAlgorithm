
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

i = 0
length = N
print("<", end="")
for _ in range(N-1):
    i = (i + K-1) % length
    print(arr[i], end=", ")
    arr.pop(i)
    length -= 1

print(arr[0], end="")
print(">", end="")
