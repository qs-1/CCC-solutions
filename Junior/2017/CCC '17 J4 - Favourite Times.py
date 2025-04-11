def arith_count(hour, mins=60):
    count = 0
    for min in range(mins+1):
        min_tens = min // 10
        min_ones = min % 10
        
        if hour < 10:  # single digit hour
            if (hour - min_tens == min_tens - min_ones):
                count += 1

        else:  # double digit hour
            hour_tens = hour // 10
            hour_ones = hour % 10
            
            if (hour_tens - hour_ones == hour_ones - min_tens == min_tens - min_ones):
                count += 1
    return count

# make mapping of hour : arithmetic sequence count 
fav = {}
for hour in range(1,13):
    fav[hour] = arith_count(hour)


time = int(input())
h = time//60
m = time%60
count = 0

# add count for hours
leftoff_hour = 12 # for mins, to find which hour we leftoff at
if h>0:
    #has cycle
    if h>=12:
        cycle = sum(x for x in fav.values())
        count = cycle*(h//12) # add cycle count
        h = h%12 # remove cycles
    
    # add leftover hours
    if h>0:
        count += 1 # handle 12 hour separately
        h -= 1
        if h == 0:
            leftoff_hour = 1 

    #now handle 1-11
    if h>0:
        for i in range(1,h+1):
            count += fav[i]
        leftoff_hour = i+1 # we'll check from next hour since prev hrs completed full 60mins each

# add count for mins (from where we last stopped)
if m>0:
    count += arith_count(leftoff_hour, m)    

print(count)