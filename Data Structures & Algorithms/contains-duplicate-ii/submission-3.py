class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val_idx_pair = {}

        for i, val in enumerate(nums):
            if val in val_idx_pair:
                if i - val_idx_pair.get(nums[i]) <= k:
                    return True
            
            val_idx_pair[nums[i]] = i

        return False

