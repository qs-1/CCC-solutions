N = int(input())
data = []
for _ in range(N):
    line = input()
    data.append(list(map(int, line.split())))

# print(data)
# For example, if input is:
# 3
# 4 3 1
# 6 5 2
# 9 7 3
# then data will be:
# [[4, 3, 1], [6, 5, 2], [9, 7, 3]]

# make sure first row ascending
# make sure first column descending


found = False
while not found:
    for y in range(4):
        if data[0][0] < data[0][-1] and data[0][0] < data[-1][0]:
            #found correct
            found = True
            break 

        clockwise = []
        for i in range(len(data[0])): # for every col
            new_row = []
            
            for j in range(len(data)): # make a new row of the column
                new_row.append(data[j][i])

            clockwise.append(new_row[::-1]) # need to reverse the row order otherwise we only took transpose

        data = clockwise

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j], end = ' ')
    print()