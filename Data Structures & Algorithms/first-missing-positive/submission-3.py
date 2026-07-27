class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()

        target = 1
        for n in nums:
            if n == target:
                target += 1
        
        return target

