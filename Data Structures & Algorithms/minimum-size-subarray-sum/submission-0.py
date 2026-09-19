class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        l = 0
        currSum = 0

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target and l <= r:
                min_length = min(min_length, r-l+1)
                currSum -= nums[l]
                l += 1

        return 0 if min_length == float("inf") else min_length
