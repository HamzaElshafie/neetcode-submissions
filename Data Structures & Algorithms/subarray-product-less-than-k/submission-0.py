class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prod = 1
        res = 0

        if k <= 1:
            return 0

        for r in range(len(nums)):
            prod *= nums[r]

            # current window exceeded threshold
            while prod >= k:
                prod /= nums[l]
                l += 1
            
            # current window is now valid

            res += (r - l) + 1
        
        return res

