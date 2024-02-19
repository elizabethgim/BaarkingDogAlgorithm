
T = int(input())

for _ in range(T):
    string = input()
    stack = []
    flag = False
    for s in string:
        if s == "(":
            stack.append("(")
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = True
                break

    if stack:
        print("NO")
    else:
        if flag:
            print("NO")
        else:
            print("YES")
