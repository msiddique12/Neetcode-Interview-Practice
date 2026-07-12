import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create maxHeap of stones
        #run a while loop whilst len(heap) > 1
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            if x == y:
                continue
            else:
                newWeight = -1 * (x-y)
                heapq.heappush(stones, newWeight)
        
        if len(stones) == 1:
            return -1 * stones[0]
        return 0


