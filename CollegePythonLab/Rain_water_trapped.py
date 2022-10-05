def maxWater(arr, n):

    res = 0
    for i in range(1, n - 1):

        l = arr[i]
        for j in range(i):
            l = max(l, arr[j])

        r = arr[i]
 
        for j in range(i + 1, n):
            r = max(r, arr[j])

        res = res + (min(l, r) - arr[i])
 
    return res
 
 


        
