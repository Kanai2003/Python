#function to find Sum_Of_Triplet
def Sum_Of_Triplet(A, n, X):

        triple=0

        for i in range(0,n):

            for j in range((i+1),n):

                for k  in range((j+1),n):

                    if A[i]+A[j]+A[k]==X:

                        triple+=1

        return triple
#array
A=[1,4,45,6,10,8]
#function calling
print(Sum_Of_Triplet(A, 6, 13 ))
