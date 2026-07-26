class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int) # key: number, value: freq in nums

        for n in nums:
            freq_map[n] += 1
        
        freq_list = []
        for key, v in freq_map.items():
            freq_list.append((v, key))
        

        freq_list.sort(reverse=True)
        print(freq_list)

        res = []
        for i in range(k):
            print(i)
            res.append(freq_list[i][1])
        print(res)

        return res








        








