m=int(input("Enter no of rows: "))
n=int(input("Enter no of columns: "))
print("Enter Elements: ")
mat=[[int(input()) for x in range(n)] for y in range(m)]
print("Square Matrix is: ")
for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()

print("Transpose of the matrix is: ")
for i in range(n):
    for j in range(m):
        print(mat[j][i],end=" ")
    print()