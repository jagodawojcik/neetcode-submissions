class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        all_freq_pairs = []
        for num, freq in freq_map.items():
            all_freq_pairs.append((freq, num))

        all_freq_pairs.sort(reverse=True)

        result = []
        for p in all_freq_pairs:
            result.append(p[1])
            if len(result) == k:
                return result

        return result





