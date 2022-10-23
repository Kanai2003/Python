N = int(input("Enter size of the array : "))
z=list()
for i in range(N):
    z.append(int(input("Enter element : ")))
M = int(input("Enter value of M : "))
z.sort()
print("M th smallest element is : ",z[M-1])
print("M th largest element is : ",z[-M]) 