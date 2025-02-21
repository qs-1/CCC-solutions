memo={}
def rule_of_3(steps,sequence,final,path=[]):
    if (steps,sequence) in memo:
        return memo[(steps,sequence)]

    #base case if out of steps
    if steps == 0:
        return path if sequence == final else False
    
    #apply all possible rules for each index
    result = None
    sequence_length = len(sequence)
    for i in range(sequence_length):
        
        for n in rules:
            #for example for AA → AB
            #AA is rule input
            #Ab is rule output
            rule_input = rules[n][0]
            rule_output = rules[n][1]

            if len(rule_input) <= sequence_length-i: #check if length of rule sequence is enough to fit within index and end
                if rule_input == sequence[i:i+len(rule_input)]:#now check if rule sequence matches sequence at index 

                    new_sequence = sequence[:i] + rule_output + sequence[i+len(rule_input):]
                    path.append((n, i, new_sequence))

                    result = rule_of_3(steps-1,new_sequence,final,path)
                    if result:
                        return path
                    path.remove((n, i, new_sequence))                 
    memo[(steps,sequence)] = result
    return []


rules = {}
for i in range(3):
    line = input().split()
    rules[i] = [line[0],line[1]]    
steps, sequence, final = input().split()
steps = int(steps)

path = rule_of_3(steps,sequence,final)
for curr in path:
    r, p, w = curr
    print(r+1, p+1, w)
