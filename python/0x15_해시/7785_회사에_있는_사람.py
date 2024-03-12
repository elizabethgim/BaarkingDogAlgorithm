'''
input => 4128ms
sys.stdin.readline 사용 O => 240ms
'''

N = int(input())
company = {}

for _ in range(N):
    name, status = input().strip().split()
    if status == "enter":
        company[name] = True
    else:
        company[name] = False

company = sorted(company.items(), key=lambda x:x[0], reverse=True)

for n, c in company:
    if c:
        print(n)

'''
import sys
N = int(sys.stdin.readline())
ppl = {}

for _ in range(N):
    name, action = sys.stdin.readline().strip().split()

    if action == "enter":
        ppl[name] = action
    else:
        ppl.pop(name)

print(*sorted(ppl, reverse=True), sep='\n')
'''