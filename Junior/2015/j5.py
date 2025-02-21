############################    J-5
memo = {}
def countways(current_index, curr_min_pieces, remaining_pieces,people):
    #is remaining_pieces enough to give each next index atleast curr_min_pieces required?
    #
    if curr_min_pieces*(people-current_index) > remaining_pieces:
        return 0

    #check if this state was encountered before
    call = (current_index, curr_min_pieces, remaining_pieces)
    if call in memo:
        return memo[call]

    #base case
    if current_index == people-1: #last person
        return 1
    
    #for current index check all valid pieces we can give
    ways = 0
    MaxPieces = remaining_pieces // people - current_index 
    for i in range(curr_min_pieces, MaxPieces): #from 1 to remaining
        #basically considering all possible pieces we can give to this person at index i

        #go 1 position forward, update min pieces we have to give to rest to the pieces we just
        #gave to current person and update new remaining pieces
        ways += countways(current_index+1, i, remaining_pieces-i) 

    #save the output for this state
    memo[call] = ways
    return ways

n=250
k=250
print(countways(0,1,n,k))