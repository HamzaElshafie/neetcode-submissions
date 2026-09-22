class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        curr_prod = 1
        for l in range(1,len(nums)):
            curr_prod *= nums[l-1] # 2
            left[l] = curr_prod
        
        curr_prod = 1
        for r in range(len(nums)-2, -1, -1):
            curr_prod *= nums[r+1]
            right[r] = curr_prod

        return [a * b for a, b in zip(left, right)]
