class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            # Invalid array
            if l > r:
                return -1

            # Calculate middle index 
            mid_idx = l + (r - l) // 2

            if target > nums[mid_idx]:
                # Explore right subarray
                return binary_search(mid_idx+1, r)
            elif target < nums[mid_idx]:
                # Explore left subarray
                return binary_search(l, mid_idx-1)
            else:
                return mid_idx

        return binary_search(0, len(nums)-1)