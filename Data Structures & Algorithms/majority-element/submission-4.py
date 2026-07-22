class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq_map = defaultdict(int)

        for n in nums:
            freq_map[n] += 1
            if freq_map[n] >= len(nums) / 2:
                return n
