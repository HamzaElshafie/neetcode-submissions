import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count occurances of ints in nums
        counts = {}
        for val in nums:
            counts[val] = 1 + counts.get(val, 0)

        data = []
        for key, value in counts.items():
            heapq.heappush(data, (value, key))

            if len(data) > k:
                heapq.heappop(data)
        
        return [number for frequency, number in data]
        