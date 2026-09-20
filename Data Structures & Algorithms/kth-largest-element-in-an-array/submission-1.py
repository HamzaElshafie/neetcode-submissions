import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
        
# so obv we can sort using merge sort or smth and then return the element at the kth index but the question explicitly asks to not sort

# Approach
# use a max heap to first put them in the correct order we want
# we pop from it k times and then return the last popped value

# Input: nums = [2,3,1,5,4], k = 2

# [-5,-4,-3,-2,-1]     k = 0, 1