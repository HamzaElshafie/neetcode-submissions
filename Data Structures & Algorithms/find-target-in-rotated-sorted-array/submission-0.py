# nums = [1,2,3,4,5,6] -> target = 2
# [3,4,5,6,1,2] if it was rotated 4 times.
# [3,4,5 | 6,1,2] 

# Find the sorted half.

# If target fits inside that half's value range:
#     search the sorted half.
# Otherwise:
#     search the other half.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # find the sorted half
            if nums[l] <= nums[mid]:
                # left half is sorted
                if nums[l] <= target < nums[mid]:
                    # search the left half
                    r = mid - 1
                else:
                    # search the right half
                    l = mid + 1
            else:
                # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1
            
            
        