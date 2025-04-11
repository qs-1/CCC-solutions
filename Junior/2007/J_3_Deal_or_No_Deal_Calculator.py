dolla = {1:100,  2:500, 3:1000 , 4:5000,
          5:10000, 6:25000, 7:50000,
            8:100000, 9:500000, 10:1000000}

opened = int(input())

for i in range(opened):
    n = int(input())
    dolla.pop(n)

banker = int(input())

rem = sum(dolla.values()) / len(dolla)
print('deal' if banker >= rem else 'no deal')