class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0 # The time it takes for the current fleet leader to finish
        
        for p, s in cars:
            arrival_time = (target - p) / s
            # If this car takes LONGER than the current fleet leader,
            # it cannot catch up, so it starts a new fleet.
            if arrival_time > max_time:
                fleets += 1
                max_time = arrival_time
                
        return fleets
        # pair = [[p,s] for p,s in zip(position, speed)]
        # stack = []

        # for p,s in sorted(pair)[::-1]: #Reverse sorted order
        #     stack.append((target - p) / s)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)

