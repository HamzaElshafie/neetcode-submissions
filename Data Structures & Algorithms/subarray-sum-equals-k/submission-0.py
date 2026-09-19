class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        prefixSums = {0: 1}
        total = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in prefixSums:
                # We found a subarray
                total += prefixSums.get(diff)
            
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return total