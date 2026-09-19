class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            # Pop y, then x
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x != y:
                new_w = y - x
                heapq.heappush(stones, -new_w)
        
        return -heapq.heappop(stones) if len(stones) == 1 else 0