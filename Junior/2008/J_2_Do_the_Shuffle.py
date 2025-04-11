lst = list('ABCDE')

while True:
    b = int(input())
    n = int(input())
    
    if b==4 and n==1:
        print(*lst)
        break

    if b == 1:
        for i in range(n):
            lst = lst[1:] + [lst[0]]
            
    if b == 2:
        for i in range(n):
            lst = [lst[-1]] + lst[:-1]

    if b == 3:
        lst[0], lst[1] = lst[1], lst[0]