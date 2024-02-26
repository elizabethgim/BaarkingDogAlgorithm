from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    task = input().split()

    if task[0] == "push":
        queue.appendleft(int(task[1]))

    elif task[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif task[0] == "size":
        print(len(queue))

    elif task[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif task[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

    elif task[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
