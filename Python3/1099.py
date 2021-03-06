__________________________________________________________________________________________________
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        maxx = -float('inf')
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if maxx < A[i] +A[j] and A[i] + A[j] < K:
                    maxx = A[i] + A[j]
        return maxx if maxx != -float('inf') else -1
__________________________________________________________________________________________________

__________________________________________________________________________________________________
