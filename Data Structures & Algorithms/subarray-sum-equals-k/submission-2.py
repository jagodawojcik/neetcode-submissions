class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix_sum = defaultdict(int) 

        prefix_sum[0] = 1

        sum_count = 0
        for n in nums:
            sum_count += n
            if sum_count - k in prefix_sum:
                res += prefix_sum[sum_count - k]
            prefix_sum[sum_count] += 1

        return res


