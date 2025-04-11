dist = list(map(int, input().split()))

for i in range(5):
    curr = [-1]*5

    prefix = []
    suffix = []
    for j in range(i-1,-1,-1):
        suffix.append((suffix[-1] if suffix else 0) + dist[j])
    for k in range(i,4):
        prefix.append((prefix[-1] if prefix else 0) + dist[k])



    print(*(suffix[::-1]+[0]+prefix))