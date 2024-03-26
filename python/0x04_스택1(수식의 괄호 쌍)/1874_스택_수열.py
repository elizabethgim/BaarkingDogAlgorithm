import sys
input = sys.stdin.readline
n = int(input())
stack = []
answer = []
i = 1
can = True

for _ in range(n):
    nn = int(input())

    while i <= nn:
        stack.append(i)
        answer.append('+')
        i += 1

    if stack[-1] == nn:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        can = False
        break

if can:
    print(*answer, sep="\n")



