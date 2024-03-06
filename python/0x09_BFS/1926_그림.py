'''
시간: 368ms
메모리: 35888KB
'''

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(start):
    que = deque()
    que.append(start)
    cnt = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 1:
                        cnt += 1
                        que.append((nx, ny))

    return cnt


cnt_picture = 0
max_picture = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt_picture += 1
            max_picture = max(max_picture, bfs((i, j)))

print(cnt_picture)
print(max_picture)
