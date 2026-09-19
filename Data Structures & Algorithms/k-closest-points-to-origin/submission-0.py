class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        closest = []
        for i in range(len(points)):
            cur_dist = self.euclidean_distance(points[i], [0,0])
            distances.append((cur_dist, i))
        
        heapq.heapify(distances)

        for _ in range(k):
            cur = heapq.heappop(distances)
            closest.append(points[cur[1]])
        
        return closest
    
    def euclidean_distance(self, point1, point2):
        """
        Calc euclidean distance between point and origin
        """
        return math.sqrt(((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))
