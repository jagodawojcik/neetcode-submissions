class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}
        

        for i, n in enumerate(nums):
            if n in diffs:
                return [diffs[n], i]
            
            difference = target - n
            diffs[difference] = i


