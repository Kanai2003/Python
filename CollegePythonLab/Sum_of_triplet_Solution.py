# Sum of triplet solution 
def sum_of_triplet(n , m , arr):
    for i in range(0 , n):
        for j in range(0 , len(arr)):
            x = m - (arr[i] + arr[j])
            if(x in arr and x!= arr[i] and x!= arr[j]):
                print(arr[i] , arr[j] , x)
                break
        break

arr = [1,4,45,6,10,8]
sum_of_triplet(6,13,arr)
