
def maxArea(A):
        l = 0
        r = len(A) -1
        area = 0

        while l < r:
            # Calculating the max area
            blk=sum(A[l+1:l+r-1])
            area = max(area, min(A[l],A[r]) * (r - l-1)-blk)

            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        
        return area
a=[3,0,2,0,4]
print(maxArea(a))
