N = int(input())
data = []
for _ in range(N):
    line = input()
    data.append(list(map(int, line.split())))

def rotate(arr):
    return list(zip(*arr[::-1]))

# make sure first row ascending
# make sure first column descending

found = False
while not found:
    for y in range(4):
        # valid found
        if data[0][0] < data[0][-1] and data[0][0] < data[-1][0]:
            found = True
            break 
        # rotate clockwise:
        # data[::-1] reverses order of rows
        # transpose (rows into cols):
        # * operator unpacks rows and passes rows to zip(row1,row2...)
        # zip() returns elements by position (index 0 of row1,row2..., index 2 of row1,row2...)
        data = list(zip(*data[::-1])) 

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j], end = ' ')
    print()


# manual rotation
        # clockwise = []
        # for i in range(len(data[0])): # for every col
        #     new_row = []
            
        #     for j in range(len(data)): # make a new row of the column
        #         new_row.append(data[j][i])

        #     clockwise.append(new_row[::-1]) # need to reverse the row order otherwise we only took transpose

        # data = clockwise