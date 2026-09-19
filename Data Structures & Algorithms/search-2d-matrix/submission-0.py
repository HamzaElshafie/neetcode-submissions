class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Edge case
        if not matrix or matrix[0][0] > target:
            return False

        row_ptr = None
        # Find row to search in
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                row_ptr = i
                break

        if row_ptr is None:
            return False
        
        return binary_search(matrix[row_ptr], target, 0, len(matrix[0])-1)

def binary_search(nums, target, l, r):
    if l > r:
        return False
    
    middle_idx = l + (r-l) // 2

    if target > nums[middle_idx]:
        return binary_search(nums, target, middle_idx + 1, r)
    elif target < nums[middle_idx]:
        return binary_search(nums, target, l, middle_idx - 1)
    return target == nums[middle_idx]
        