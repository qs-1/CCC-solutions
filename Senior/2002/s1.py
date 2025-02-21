tickets = []
for i in range(4):
    tickets.append(int(input()))

amount = int(input())


# need to find number of combinations that make amount
combos = []
def combinations(p=0, g=0, r=0, o=0, index=0, curr=None):
    if curr is None:
        curr = amount 

    if curr == 0:
        combos.append((p, g, r, o))
        return

    if curr < 0:
        return

    # fix the choice at each index, so we cant change it later (gets rid of repition)
    """
    Once you pick a ticket from a given index, 
    subsequent recursive calls only consider 
    that index or higher, which forces an
    order (for example: all PINKs first, then
    GREENs, etc.) so that (1,1,0,0) is only 
    generated one way (1 PINK first then 
    1 GREEN) and not (1 GREEN then 1 PINK
    since we cant go back from 2nd index and
    change that choice now, this wouldve been
    possible without using a loop which fixes
    indices)
    """
    for i in range(index,4): # skip the previous part since we fixed those choices 
        if i == 0:
            combinations(p + 1, g, r, o, i, curr - tickets[0])
        elif i == 1:
            combinations(p, g + 1, r, o, i, curr - tickets[1])
        elif i == 2:
            combinations(p, g, r + 1, o, i, curr - tickets[2])
        else:
            combinations(p, g, r, o + 1, i, curr - tickets[3])


combinations()
    
mintickets = float('inf')
for combo in combos:
    mintickets = min(mintickets, sum(combo))
    print(f"# of PINK is {combo[0]} # of GREEN is {combo[1]} # of RED is {combo[2]} # of ORANGE is {combo[3]}")

print(f"Total combinations is {len(combos)}.")
print(f"Minimum number of tickets to print is {mintickets}.")