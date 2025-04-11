n = int(input())
r,c = map(int, input().split())
A = []
for z in range(r):
    A.append(list(map(int, input().split())))

for _ in range(n-1):
    r2,c2 = map(int, input().split())
    B = []
    for z in range(r2):
        B.append(list(map(int, input().split())))

    tensor = []
    for i in range(r):
        for br in range(r2):
            newrow = []
            for j in range(c): #for each row, each A column gets multiplied all B columns
                for XX in range(c2):
                    newrow.append(A[i][j]*B[br][XX] )
            tensor.append(newrow)
    #new matrix for next multipication A ⊗ B ⊗ C, now TensorProd ⊗ C ...
    A = tensor
    r = len(tensor)
    c = len(tensor[0])
 
    # for cc in A:
    #     print(*cc)   

# the maximum element in the tensor product
print(max(max(row) for row in A))
# the minimum element in the tensor product
print(min(min(row) for row in A))
# the maximum row sum (i.e., sum of entries in each row)
print(max(sum(row) for row in A))
# the minimum row sum
print(min(sum(row) for row in A))
# the maximum column sum
print(max(sum(col) for col in zip(*A)))
# the minimum column sum
print(min(sum(col) for col in zip(*A)))