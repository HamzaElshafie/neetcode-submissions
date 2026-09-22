class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        curr_prod = 1
        for l in range(len(nums)):
            out[l] *= curr_prod
            curr_prod *= nums[l]
        
        curr_prod = 1
        for r in range(len(nums)-1, -1, -1):
            out[r] *= curr_prod
            curr_prod *= nums[r]

        return out
