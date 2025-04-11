free = int(input())
n = int(input())
intervals = [list(map(int,input().split())) for i in range(n)]
intervals.sort() # so overlapping intervals are consecutive

#now check for the largest gap between intervals
maxx = 0

if intervals[0][0] > 0: # check for free space in start
    maxx = max(maxx, intervals[0][0])

longest_end = intervals[0][1]
for i in range(1,n): # check gap in between intervals
    if intervals[i][0] > longest_end:
        maxx = max(maxx, abs(intervals[i][0] - longest_end))
        longest_end = intervals[i][1] # next intervals start compared with the end of this as this created a gap and thus is the new longest end 

    else: # overlap case, update with new bigger interval if new end is longer
        longest_end = max(longest_end, intervals[i][1])

if intervals[-1][1] < free: # check for gap after the last interval
    maxx = max(maxx, abs(intervals[-1][1] - free))

print(maxx) # print the largest gap