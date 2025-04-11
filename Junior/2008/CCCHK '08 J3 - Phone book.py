phonebook = {}
numpairs = int(input())

for i in range(numpairs):
    name, num = input().split()
    num = int(num)
    phonebook[num] = name

# print(phonebook)

numdialed = int(input())
hashcnt = {}
for j in range(numdialed):
    num = int(input())
    if num not in hashcnt:
        hashcnt[num] = 0
    hashcnt[num] += 1

# print(hashcnt)

maxx = max(hashcnt.values())

maxsame = []
for key in hashcnt:
    if hashcnt[key] == maxx:
        maxsame.append(key)

print(phonebook[min(maxsame)])