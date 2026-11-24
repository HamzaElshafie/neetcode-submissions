class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(logn)
        res = set()

        # pin each number and try finding triplets
        for i in range(len(nums)):
            pinned_num = nums[i]

            # start two ptrs from opposite ends
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = -pinned_num # 4
                if nums[l] + nums[r] == target:
                    if (pinned_num, nums[l], nums[r]) not in res:
                        res.add((pinned_num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target: # make bigger
                    l += 1
                else:
                    r -= 1

        return list(res)


# Input: nums = [-1,0,1,2,-1,-4]

# ORDERED = [-4,-1,-1,0,1,2]

# Output: [[-1,-1,2],[-1,0,1]]

# pinned = -1
# l = 2
# r = 5