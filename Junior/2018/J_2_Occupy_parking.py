n = int(input())
yest = input()
tod = input()

cnt = 0
for i in range(n):
    if yest[i] == 'C' and tod[i] == 'C':
        cnt += 1

print(cnt)