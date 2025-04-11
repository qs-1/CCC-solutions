n = int(input())
k = int(input())


ans = 0
for i in range(k+1):
    ans = ans + n
    n = n*10

print(ans)