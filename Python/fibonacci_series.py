# Program to print fibonacci series for given n terms

n = int(input("Enter terms:"))

i = 0
j = 1
print(i,j,end=" ")
for num in range(n):
    k = i+j
    i = j
    j = k
    print(k,end=" ")
