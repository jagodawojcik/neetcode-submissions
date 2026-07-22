class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique_nums = {}
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums[num] = 1
        return False