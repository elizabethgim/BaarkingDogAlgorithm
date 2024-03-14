n = int(input())
stack = []
i = 1
stack.append(i)

for _ in range(n):
    nn = int(input())

    if nn == i:
        print("-")
    else:
        while stack[-1] < nn:
            i += 1
            stack.append(i)

        print("+")



