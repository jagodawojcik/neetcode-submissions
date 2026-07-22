class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        num_set = set(nums)

        count = 0
        longest = 0
        for n in num_set:
            count = 1
            next_num = n + 1
            while next_num in num_set:
                count += 1
                next_num += 1
            longest = max(longest, count)

        return longest

            


