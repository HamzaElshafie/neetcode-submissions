class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialise array to be of all ones len(nums)
        answer = [1] * len(nums)
        # Iterate on nums to build prefix from i = 2 (len(nums)+1)
        for i in range(1, len(nums)):
            # Multiply current nums[index] with the prefix at [index-1]
            # and save in index
            answer[i] = answer[i-1] * nums[i-1]

        # Pass in reverse to accumilate answer
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer