class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        freq_list = [[] for i in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            freq_list[freq].append(num)

        result = []
        for el in freq_list[::-1]:
            if len(result) >= k:
                break
            result.extend(el)

        return result[:k+1]









        








