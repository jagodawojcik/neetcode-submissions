class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target_n = {}

        for i, n in enumerate(nums):
            if n in target_n:
                return [target_n[n], i]   
            target_n[target - n] = i
        return []
            

