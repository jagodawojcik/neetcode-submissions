class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums_set = set(nums)

        longest_count = 0
        count = 0
        for n in nums_set:
            count = 0
            while n in nums_set:
                count += 1
                n += 1
            longest_count = max(count, longest_count)

        return longest_count