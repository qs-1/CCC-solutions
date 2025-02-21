inp = int(input())


#probably shouldve hardcoded the counts for 12 hours, simulated to make those instead


def count_valid_minutes(curr_hour, max_minute=60):
    count = 0
    for j in range(1, 60 if max_minute == 60 else max_minute+1): # could be less than 60 for the final hour, like for 1hr 20 min, we count hr normally, but for 2nd hour we stop at 20
        ignore = False
        if curr_hour < 10:  # ignore starting 0 in the time like 1:00
            diff = abs(curr_hour % 10 - j // 10)
            ignore = True
        else:
            diff = abs(curr_hour % 10 - curr_hour // 10)
        diff *= -1 if j // 10 > j % 10 else 1

        if (curr_hour % 10) + diff == (j // 10) and (j // 10) + diff == j % 10:
            if not ignore:
                if curr_hour % 10 == (curr_hour // 10) + diff:
                    count += 1
            else:
                count += 1
    return count



def favTimes(inp):
    if inp == 0:
        print(0)
        return


    mins = inp % 60 
    hours = inp // 60


    if mins >= 34 and hours==0:
        print(1)
        return

    
    count = 0
    curr_hour = 12
    prefixSum = [1]

    bound = min(12, hours)  # incase more than 12 hours (will add those leftover hours separately using the prefixsums we built)

    while bound > 0:

        if curr_hour == 12:  # add 1 for this since only one sequence
            count += 1
            curr_hour = 1  # 12 to 1pm

        else:  # for all other hours 1 to 11
            count += count_valid_minutes(curr_hour)
            prefixSum.append(count)
            if curr_hour == 11:
                curr_hour = 12  # reset the 1 to 11 clock
            else:
                curr_hour += 1  # should not happen for 12pm, manually setting it to 1 in if block

        bound -= 1  # 1 hour looking completed





    parts = hours // 12

    if parts != 0: # #update incase more sets of 12 exactly hours
        count *= parts 

    # now check if any leftover hours or minutes

    leftover = (hours % 12) if parts!=0 else 0 # any leftover for instance 3 for 15hrs IGNORE IF ONLY 12 HOURS OR LESS

    if leftover > 0: # 1 hour or more left
        count += prefixSum[leftover-1]

    if mins > 0: # any mins left? (all hours covered by above parts and leftover)
        if leftover == 0: # if there were no leftover hours then it means we last stopped at 12 (we know only 1 arithmetic sequence 12:34 so add that if enough mins)
            count += 1 if mins >= 34 else 0

        else: # otherwise were between 1 - 11 pm and have some mins left so check if any sequence for that too
            count += count_valid_minutes(leftover, mins) 

    print(parts,leftover,mins,count)

favTimes(inp)



