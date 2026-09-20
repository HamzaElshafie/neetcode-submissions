import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        # contruct max heap
        for weight in stones:
            heapq.heappush(heap, -weight)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            elif x != y:
                new_w = x-y
                heapq.heappush(heap, -new_w)

        return -heapq.heappop(heap) if heap else 0

# [2,3,6,2,4]
# max_heap = [-6,-4,-3,-2,-2]

x = 6
y = 4

# Because we have the wording two heaviest stones, we will use a max heap
# every step we pop two values from the heap
# We need also a way of inserting into the max heap after we alter smash the weights and we need to put the new weight into the heap