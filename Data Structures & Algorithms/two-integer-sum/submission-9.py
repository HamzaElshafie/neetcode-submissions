class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, val in enumerate(nums):
            if val not in num_to_idx:
                num_to_idx[val] = i
        
        for idx, num in enumerate(nums):
            rem = target - num
            if rem in num_to_idx and idx != num_to_idx[rem]:
                return sorted([idx, num_to_idx[rem]])