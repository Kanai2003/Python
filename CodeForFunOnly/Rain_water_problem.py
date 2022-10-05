class Solution:
# @param A, a list of integers
# @return an integer

 def trap(self, A):
    if not A: return 0
    res, l, r = 0, [A[0]] * len(A), [A[len(A) - 1]] * len(A)
    for i in range(1, len(A)): 
        l[i], r[-i - 1] = max(A[i], l[i - 1]), max(A[-i - 1], r[-i])
    for i in range(1, len(A) - 1):
        res += max(0, (min(l[i - 1], r[i + 1]) - A[i]))
    return res