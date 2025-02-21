
n = int(input().strip())

m = [None]  # to make it 1-indexed

for i in range(n):
    m.append(int(input().strip())) # initial streams

while True:
    operation = int(input().strip())

    if operation == 77: # end
        break

    if operation == 99:  # split
        stream = int(input().strip())

        # find amount of water on left and rifht fork
        l = (m[stream]*int(input().strip())) // 100
        r = m[stream] - l

        # overwrite stream with r, and then insert l at that index so order becomes l then r
        m[stream] = r
        m.insert(stream, l)

    if operation == 88: # join
        stream = int(input().strip())

        # only combime with right stream when there is a right one
        if stream < len(m)-1:
            # add water for both
            combined = m[stream] + m[stream+1]

            # remove the stream so right one moves to stream index            
            m.pop(stream)

            # now overwrite the moved over right stream with new combined value
            m[stream] = combined

print(*m[1:]) #same thing as using a loop with end = ' '
