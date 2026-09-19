class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        best = 0

        while l <= r:
            mid = (l + r) // 2
            candidate = mid * mid

            if candidate <= x:
                best = mid
                l = mid + 1
            else:
                r = mid - 1
            
        return best



