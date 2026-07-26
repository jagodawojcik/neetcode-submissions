class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using buckets, no sort. More memory but O(n) instead of O(nlogn)
        freq_list = [[] for i in range(len(nums) + 1)]

        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        for key, val in count.items():
            freq_list[val].append(key)

        res = []
        for nums in freq_list[::-1]:
            res.extend(nums)
            if len(res) >= k:
                break
        


        return res[:k]


        








        








