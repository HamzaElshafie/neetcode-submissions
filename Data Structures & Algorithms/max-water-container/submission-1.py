class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        l = 0
        r = len(height) - 1
        while l < r:
            distance = r - l 
            area = distance * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area