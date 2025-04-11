x = int(input())
y = int(input())

cnt = 0
for i in range(1, x+1):
    if (10 - i) <= y and not (10 - i < 1): 
        cnt += 1

if cnt == 0:
    print("There are 0 ways to get the sum 10.")

elif cnt == 1:
    print(f"There is 1 way to get the sum 10.")

else:
    print(f"There are {cnt} ways to get the sum 10.")