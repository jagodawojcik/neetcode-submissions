class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        len_max_seq = 0
        len_seq = 0
        for n in nums:
            len_seq = 1
            if n - 1 not in set_nums:
                next_num = n + 1
                while next_num in set_nums:
                    len_seq += 1
                    next_num += 1
                len_max_seq = max(len_seq, len_max_seq)

        return len_max_seq



            