class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq_map = {}

        majority_threshold = len(nums) // 2
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
            if freq_map[n] > majority_threshold:
                return n