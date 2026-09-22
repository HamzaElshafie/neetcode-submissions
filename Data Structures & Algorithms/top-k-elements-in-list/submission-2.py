import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count occurances of ints in nums
        counts = {}
        for val in nums:
            counts[val] = 1 + counts.get(val, 0)

        data = []
        for key, value in counts.items():
            data.append((-value, key))
        heapq.heapify(data)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(data)[1])
        
        return res
        