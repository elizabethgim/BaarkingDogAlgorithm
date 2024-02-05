import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start):
    que = deque()
    que.append(start)

    while que:
        x, y = que.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs((i, j))
                answer += 1

    print(answer)

'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''