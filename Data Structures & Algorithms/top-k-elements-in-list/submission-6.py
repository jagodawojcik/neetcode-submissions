class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # freq_list = [[]] * (len(nums) + 1)
        freq_list = [[] for i in range(len(nums) + 1)]

        

        freq_mapping = {}

        for num in nums:
            freq_mapping[num] = freq_mapping.get(num, 0) + 1

        
        for num, freq in freq_mapping.items():
            freq_list[freq].append(num)

        results = []
        for i in range(len(freq_list) - 1, 0, -1):
            if len(freq_list[i]) > 0:
                results.extend(freq_list[i])
                if len(results) >= k:
                    return results[:k]

        return results







