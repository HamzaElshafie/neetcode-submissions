class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i in range(len(nums)):
            num_set[nums[i]] = i

        {
            2: 0,
            5: 1,
            11: 3
        }

        for j in range(len(nums)):
            target_val = (target - nums[j])
            i = num_set.get(target_val)
            if target_val in num_set and j != i:
                return [i,j] if i < j else [j,i]