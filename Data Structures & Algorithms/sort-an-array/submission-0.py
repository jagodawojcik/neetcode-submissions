class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        buckets = [[] for _ in range(100_001)]
        for n in nums:
            buckets[n + 50_000].append(n)
        res = []
        for b in buckets:
            if b:
                res.extend(b)
        return res