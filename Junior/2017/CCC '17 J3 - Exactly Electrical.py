x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
bat = int(input())

dist = abs(x2-x1) + abs(y2-y1)

if bat < dist:
    print('N')

else: 
    #otherwise both need to have same parity
    # odd - odd = even
    # even - even = even too
    if (bat - dist)%2 == 0:
        print('Y')
    else:
        print('N')
