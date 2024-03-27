from collections import deque
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(int(i) for i in input()))

visited = [[False for _ in range(M)] for _ in range(N)]
count = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(start):
    queue = deque()
    queue.append(start)
    count[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1 and visited[nx][ny] is False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count[nx][ny] = count[x][y] + 1


bfs((0, 0))
print(count[N-1][M-1])
