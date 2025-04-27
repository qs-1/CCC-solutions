n, k = list(map(int, input().split()))
s = list(input())
s.append("0") # to handle run of 1s at end of s 

# initial cleanup and finding 1s positions
onesEnd = []
ones = 0
for i in range(len(s)-1):
    if s[i] == "1" and s[i+1] == "1": # still within run of 1s, mark 0
        s[i] = 0    
    elif s[i] == "1" and s[i+1] == "0": # end of run of 1s, save location to find gap later
        ones += 1
        onesEnd.append(i)
    elif s[i] == "0": continue # 0 gap, do nothing

# find gaps between 1s
gaps = []
for j in range(1,len(onesEnd)):
    gaps.append(onesEnd[j] - onesEnd[j-1] - 1)
gaps.sort()

# fill gaps
for i in range(len(gaps)):
    if gaps[i] <= k: # can fill, 1001 becomes 1111, which is 0001, 1s count got decremented
        k -= gaps[i]
        ones -= 1
    else: break

if ones == 0: # no marbles, if we have to place exactly k then placing them together will always merge to 1
    print(0 if k==0 else 1)
else: print(ones)
