import sys
input = sys.stdin.readline

string = input()

stack = []
answer = 0
for i in range(len(string)):
    if string[i] == "(":
        stack.append("(")
    else:
        if not stack:
            continue

        stack.pop()
        if string[i-1] == "(":  # 레이저이므로 막대기 개수 추가
            answer += len(stack)
        else:   # 막대기의 끝이니까 잘려진 개수만 추가
            answer += 1

print(answer)

'''
()(((()())(())()))(())
(((


(
'''