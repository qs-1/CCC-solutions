N = int(input())

#take out last words of each verse 
verses = []
vowels = 'aeiou'

# We define the last syllable of a word to be the sequence of 
# letters from the last vowel (a, e, i, o, or u, but not y) to
#  the end of the word

for i in range(N):
    words = []
    for j in range(4):
        last = (input().lower().split()[-1])

        idx = 0
        found = False
        for x in range(len(last)):
            if last[x] in vowels:
                found = True
                idx = x

        if found:
            # print(idx)
            if idx == len(last)-1:
                last = last[-1]
                # print(last)

            else:
                last = last[idx:]

        words.append(last.lower())
    verses.append(words)
# print(verses)

# 4N LINES MAKES A VERSE
for i in range(N): # for each verse

    curr = verses[i]
    o = curr[0]
    s = curr[1]
    t = curr[2]
    f = curr[3]

    form = None
    # Perfect rhyme: the four lines in the verse all rhyme 
    if o == s == t == f:
        form = 'perfect'
        
    # even rhyme: the first two lines rhyme and the last two lines rhyme
    elif o == s and t == f:
        form = 'even'
    
    # cross rhyme: the first and third lines rhyme, as do the second and fourth
    elif o == t and s == f:
        form = 'cross'
    
    # shell rhyme: the first and fourth lines rhyme, as do the second and third
    elif o == f and s == t:
            form = 'shell'
        
    # free rhyme: any form that is not perfect, even, cross, or shell
    else:
        form = 'free'

    print(form)