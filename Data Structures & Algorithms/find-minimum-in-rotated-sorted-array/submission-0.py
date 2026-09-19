# [11,13,15,17,2,3,5,7]
# [11,13,15,17 | 2,3,5,7]
#     high        low

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l != r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # our pivot is in high (left) region, search right 
                l = m + 1
            else:
                # our pivot is in low (right) region, search left 
                r = m
        
        return nums[l]









