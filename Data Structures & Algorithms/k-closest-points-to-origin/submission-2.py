import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        min_heap = []
        res = []

        for point in points:
            # calculate distance to origin
            distance = euclidean_distance(point, origin)
            heapq.heappush(min_heap, (-distance, point))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for _ in range(len(min_heap)): # k
            point = heapq.heappop(min_heap)[1]
            res.append(point)

        return res
    
def euclidean_distance(x1, x2):
    return math.sqrt((x1[0] - x2[0])**2 + (x1[1]-x2[1])**2)


# Initial approach
# So we want to iterate over each element in `points`, calculate its distance to the origin, add it to a "min heap"

# loop k times popping from min heap, returning the val last popped once we exit loop