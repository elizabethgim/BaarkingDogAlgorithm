from collections import deque
M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]


queue = deque()

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))


visited = [[False for _ in range(M)] for _ in range(N)]

while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
            if not visited[nx][ny]:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True


notall = False
max_result = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            notall = True
            break
        else:
            max_result = max(max_result, tomato[i][j])

if max_result == 1:
    print(0)
else:
    if notall:
        print(-1)
    else:
        print(max_result - 1)
