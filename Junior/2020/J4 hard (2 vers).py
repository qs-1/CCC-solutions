####################################### longer code for understanding 
# check if any cyclic shift of S is exists in T
T = input()
S = input()

def rabin_karp(T,S):
    T_len = len(T)
    S_len = len(S)

    if T_len == 0:
        print('yes' if not S_len else 'no')
        return
        
    if S_len > T_len:
        print('no')
        return

    # RABIN - KARP (MONTE CARLO VER with double hashing)
    BASE = 33 # closest prime to number of chars 26 
    BASE2 = 137

    # also a prime since it dosen't have any factors other than 1 and itself (reduce chance of collision)
    MOD = 10**9 + 7 # will wraparound once window string in 31 base becomes this large
    MOD2 = 10**9 + 9

    # using the polynomial hash function, left to right ie. decreasing base (like in normal decimal notation i think)
    def hash_word(s,i,j,base,mod):
        hashed = 0
        for k in range(i, j):
            #multiply it by base at each step to move everything to left and then just add new char
            hashed = (hashed*base + (ord(s[k]) - ord('A'))) % mod
        return hashed

    # find hash of all cyclic shifts of S and save for checking in T (using same rolling hash logic)
    cyclic = hash_word(S,0,S_len,BASE,MOD)
    cyclic2 = hash_word(S,0,S_len,BASE2,MOD2)

    # also hash the initial window of T to begin the rolling hash
    window_hash = hash_word(T, 0, S_len, BASE, MOD)
    window_hash2 = hash_word(T, 0, S_len, BASE2, MOD2)

    

    POWER = pow(BASE , (S_len - 1),MOD)
    POWER2 = pow(BASE2 , (S_len - 1),MOD2)

    shifts = set()
    shifts.add(cyclic) # original hash
    shifts2 = set()
    shifts2.add(cyclic2)
    
    S2 = S+S
    for i in range((S_len*2) - S_len):
        left = (ord(S2[i]) - ord('A'))
        right = (ord(S2[i+S_len]) - ord('A'))
        # remove leftmost contribution
        cyclic = (cyclic - (left*POWER)) % MOD
        cyclic2 = (cyclic2 - (left*POWER2)) % MOD2

        # shift 1 to left
        cyclic = (cyclic * BASE) % MOD
        cyclic2 = (cyclic2 * BASE2) % MOD2

        # add new character
        cyclic = (cyclic + right) % MOD
        cyclic2 = (cyclic2 + right) % MOD2

        # add this shift hash to set
        shifts.add(cyclic)
        shifts2.add(cyclic2)


    # check the initial window before rolling
    if window_hash in shifts and window_hash2 in shifts2:
        print('yes')
        return

    # start rolling hash and checks
    for i in range(T_len - S_len):
        # rollover step
        left = (ord(T[i]) - ord('A'))
        right = (ord(T[i+S_len]) - ord('A'))

        # step 1: remove leftmost char's contribution (leftmost multiplied by base^(n-1))
        window_hash = (window_hash - left*POWER) % MOD
        window_hash2 = (window_hash2 - left*POWER2) % MOD2

        # step 2: shift by multiplying with base
        window_hash = (window_hash * BASE) % MOD
        window_hash2 = (window_hash2 * BASE2) % MOD2

        # step 3: add new right char (no need to multiply with base since base(^n-n) is 1 anyway)
        window_hash = (window_hash + right) % MOD
        window_hash2 = (window_hash2 + right) % MOD2

        if window_hash in shifts and window_hash2 in shifts2: 
            print('yes')
            return

    print('no')

rabin_karp(T,S)




###################################### shorter code same logic
T = input()
S = input()

def rabin_karp(T, S):
    T_len = len(T)
    S_len = len(S)

    if T_len == 0:
        print('yes' if S_len == 0 else 'no')
        return

    if S_len > T_len:
        print('no')
        return

    BASE = 33
    MOD = 10**9 + 7
    POWER = pow(BASE, S_len - 1, MOD)

    BASE2 = 137
    MOD2 = 10**9 + 9
    POWER2 = pow(BASE2, S_len - 1, MOD2)

    # compute initial hash
    def hash_word(word, m, base, mod):
        h = 0
        for ch in word[:m]:
            h = (h * base + (ord(ch) - ord('A'))) % mod
        return h

    # compute rest of the hashes using rolling hash
    def roll_hash(cur, left, right, base, power, mod):
        return ((cur - left * power) * base + right) % mod
    def rolling_hashes(s, m, base, power, mod):
        n = len(s)
        hs = []
        # Compute the initial window hash.
        cur = hash_word(s, m, base, mod)
        hs.append(cur)
        # Loop exactly n-m times, using s[i] as left and s[i+m] as the new right.
        for i in range(n - m):
            left = ord(s[i]) - ord('A')
            right = ord(s[i + m]) - ord('A')
            cur = roll_hash(cur, left, right, base, power, mod)
            hs.append(cur)
        return hs

    # compute initial hash windows for both T and S
    S2 = S + S
    cyclic_hashes1 = rolling_hashes(S2, S_len, BASE, POWER, MOD)[:S_len]
    cyclic_hashes2 = rolling_hashes(S2, S_len, BASE2, POWER2, MOD2)[:S_len]
    cyclic_set = set(zip(cyclic_hashes1, cyclic_hashes2))

    T_hashes1 = rolling_hashes(T, S_len, BASE, POWER, MOD)
    T_hashes2 = rolling_hashes(T, S_len, BASE2, POWER2, MOD2)

    # check if any window in T matches a cyclic-shift from S
    for h1, h2 in zip(T_hashes1, T_hashes2):
        if (h1, h2) in cyclic_set:
            print('yes')
            return

    print('no')

rabin_karp(T,S)