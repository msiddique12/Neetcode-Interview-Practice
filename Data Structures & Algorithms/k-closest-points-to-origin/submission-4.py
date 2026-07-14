class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #loop through points
        #calculate euc distance, and store in min heap(closes to 0)
        #heap size should not exceed k - maybe store a max heap

        # T: O(n log k)
        # S: O(n)

        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(((x)**2) + ((y)**2))
            dist *= - 1

            heapq.heappush(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [[x,y] for dist,x,y in heap]
        return res


