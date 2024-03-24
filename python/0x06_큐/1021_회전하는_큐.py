from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
arr = deque([i for i in range(1, N+1)])

answer = 0

for n in num:
    while True:
        if arr[0] == n:
            arr.popleft()
            break
        else:
            if arr.index(n) > len(arr) // 2:
                while arr[0] != n:
                    a = arr.pop()
                    arr.appendleft(a)
                    answer += 1
            else:
                while arr[0] != n:
                    a = arr.popleft()
                    arr.append(a)
                    answer += 1

print(answer)