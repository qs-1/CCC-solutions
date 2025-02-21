###########################    J-3
x = 'b'
vowels = 'aeiou'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

result = ''
for i in range(len(x)):
    if x[i] in vowels:
        result += x[i]
    
    else:
        # 1. add same consonant
        temp = x[i]


        # 2. check which closest vowel
        for j in range(26):
            if x[i] == alphabet[j]: #first find the letter we are at
                #then its check left and right
                r = j+1
                l = j-1

                right_vowel = None
                while r<26:
                    if alphabet[r] in vowels:
                        right_vowel = alphabet[r]
                        break 
                    else:
                        r+=1

                left_vowel = None
                while l>=0:
                    if alphabet[l] in vowels:
                        left_vowel = alphabet[l]
                        break 
                    else:
                        l-=1

                left_dist = abs(j - l) if left_vowel is not None else float('inf')
                right_dist = abs(j - r) if right_vowel is not None else float('inf')
                
                if left_dist <= right_dist: #if same distance, we pick left, also when left closer
                    temp += left_vowel
                else:
                    temp += right_vowel
                

                # 3. now add next consoant, if z then next also z
                if x[i] == 'z':
                    temp += 'z'
                else:
                    next_consonant = None
                    for k in range(j + 1, 26):
                        if alphabet[k] not in vowels:
                            next_consonant = alphabet[k]
                            break
                    temp += next_consonant
                break  #found the 3 letters so stop and go to next index

        result += temp #add completed 3 letters to result 
print(result)

