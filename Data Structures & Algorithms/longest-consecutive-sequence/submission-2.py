# store each value in a set
# [2,20,4,10,3,4,5] -> {2,20,4,10,3,4,5}
# at each idx, if nums[i] - 1 in set, skip it because we discovered that
# sequence already
# if not, while nums[i] + 1 in set keep going and increment length found
# increment i
# obtain global max length found


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_vals = set(nums)
        max_length = 0

        for val in distinct_vals:
            if val - 1 in distinct_vals:
                continue
            
            curr_max = 1
            next_val = val + 1

            while next_val in distinct_vals:
                curr_max += 1
                next_val += 1
            
            max_length = max(max_length, curr_max)
            
        return max_length