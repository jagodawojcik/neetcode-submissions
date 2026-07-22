class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        longest = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
                longest = max(longest, count)
            elif nums[i] == nums[i+1]:
                continue
            else:
                count = 1

        return longest

            