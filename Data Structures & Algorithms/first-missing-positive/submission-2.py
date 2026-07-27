class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        # [1,2,3]
        i = 1
        while i < len(nums) + 1: 
            if i not in nums_set:
                return i
            i += 1

        return len(nums) + 1
