class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (r + l) // 2
            total_hrs = 0
            for pile in piles:
                total_hrs += math.ceil(pile / k)
            
            if total_hrs <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
        return res