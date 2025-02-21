# fails for hard version since n^2

T = input()
S = input()
yes = False

def check_rotation(T, S):
    if not S:
        print('yes') if not T else print('no')
        return

    if S in T:
        print('yes')
        return

    for i in range(len(S)-1):
        S = S[1:] + S[0] 
        # now check if S exists in T
        if S in T:
            print('yes')
            return

    print('no')

check_rotation(T,S)

