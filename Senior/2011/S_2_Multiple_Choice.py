n = int(input())

stu = []
for i in range(n):
    stu.append(input())

cnt = 0
for j in range(n):
    ans = input()
    if stu[j] == ans:
        cnt+=1

print(cnt)