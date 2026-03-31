class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #we can leverage the sorted property
        #2 pointer approach, left pointer, right pointer
        #start left at 0, right at len(numbers), keep going until they meet
        #we are guaranteed a valid solution
        
        # if nums[l] + nums[r] == target: return [l+1,r+1]
        # if nums[l] + nums[r] < target: l += 1
        # if nums[l] + nums[r] > target: r -= 1

        # [1,2,3,4], t=3
        # 1 + 4 = 5 > 3, r-=1
        # 1+ 3 = 4 > 3, r-=1
        #1+2 = 3 == 3, return [2,3]

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1
        return []



