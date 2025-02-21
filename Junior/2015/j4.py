
###########################    J-4
M = int(input().strip())

log = []
for i in range(M):
    entry = input().strip().split()
    log.append([entry[0], int(entry[1])])

#log = [['R', '2'], ['R', '3'], ['W', '5'], ['S', '2'], ['S', '3']]

#need this dictionary cuz we have to group times by friend number so will use that as key
friend_times = {}

time = -1
i=0
while i<M:
    event = log[i][0] # 'R'
    friend = log[i][1] # 2

    if event != 'W':

        if friend not in friend_times:
            friend_times[friend] = []

        time += 1
        log[i].append(time)
        friend_times[friend].append(time)

    else:
        #-1 here since ill only append when not at wait event and in those im always incrementing
        time += friend-1 #here friend is actually wait time because event is W

    i+=1


for friend in friend_times:
    num_messages = len(friend_times[friend])
    if not num_messages % 2 == 0: #didnt reply to friend
        friend_times[friend] = -1
    else:
        #each pair is message recieved time, replied time and there can be many pairs (multiple messages)
        #time for one pair is replied - recieved and for all pairs just sum this
        all_sum = 0
        for i in range(0,num_messages,2):
            p1 = friend_times[friend][i]
            p2 = friend_times[friend][i+1]
            
            pair_sum = p2-p1
            all_sum += pair_sum

        friend_times[friend] = all_sum
        

keys = list(friend_times.keys())
keys.sort()    

for key in keys:
    print(key, friend_times[key])