N = int(input())
rope = []
total = 0

for _ in range(N):
    r = int(input())
    rope.append(r)
    total += r

rope.sort(reverse=True)

answer = [0 for _ in range(N)]
for i in range(N):
    answer[i] = rope[i] * (i+1)

print(max(answer))
