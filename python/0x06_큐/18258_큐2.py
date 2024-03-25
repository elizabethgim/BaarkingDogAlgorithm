from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    task = list(input().split())

    if task[0] == "push":
        queue.append(task[1])
    elif task[0] == "pop":
        if len(queue) == 0:
            print(-1)
    elif task[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif task[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif task[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
