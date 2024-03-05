arr = []


def bt(start, depth, num):
    if depth == 6:
        print(*arr)
        return

    for i in range(start, num):
        arr.append(S[i])
        bt(i+1, depth+1, num)
        arr.pop()


while True:
    numbers = list(map(int, input().split()))
    K = numbers[0]

    if K == 0:
        break

    S = numbers[1:]
    visited = [False for _ in range(K)]
    bt(0, 0, K)
    print()
