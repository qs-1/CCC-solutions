import sys
data = sys.stdin.read().split()
brown = int(data[0])
north = int(data[1])
yellow = int(data[2])
lim = int(data[3])

cnt = 0
out_lines = []
for i in range((lim // brown) + 1):
    for j in range((lim // north) + 1):
        current = brown * i + north * j

        if current > lim:
            break  

        max_k = (lim - current) // yellow

        for k in range(max_k + 1):
            if i + j + k == 0:
                continue
            
            cnt += 1
            out_lines.append(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")

out_lines.append(f"Number of ways to catch fish: {cnt}")
sys.stdout.write("\n".join(out_lines))