a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

n_pos = s // (a + b) * (a - b) # find full s cycles, each cycle will have forward - backward dist
left = s % (a + b) # steps left after removing cycles
n_pos += min(a,left) # add forward steps

# if all leftover completed with forward, skip, otherwise
# add backward steps (after removing the already completed forward step count)
n_pos -=  0 if left-a <= 0 else  b - (left-a)

b_pos = s // (c + d) * (c - d)
left = s % (c + d)
b_pos += min(c, left)
b_pos -= 0 if left - c <= 0 else d - (left - c)

if n_pos > b_pos:
    print("Nikky")
elif b_pos > n_pos:
    print("Byron")
else:
    print("Tied")