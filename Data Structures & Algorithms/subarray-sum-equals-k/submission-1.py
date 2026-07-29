class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix_sum_count = defaultdict(int) #key: prefix_sum, val: count
        prefix_sum_count[0] += 1

        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            diff = prefix_sum - k 
            if diff in prefix_sum_count:
                res += prefix_sum_count[diff]
            prefix_sum_count[prefix_sum] += 1

        return res

            



        