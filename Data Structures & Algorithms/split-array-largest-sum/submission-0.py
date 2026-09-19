class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # possible result: minimum: 18, largest: sum of all elements
        def can_split(largest):
            subarray = 1
            cur_sum = 0

            for n in nums:
                if cur_sum + n > largest:
                    subarray += 1
                    cur_sum = 0
                
                cur_sum += n

            return subarray <= k

        l, r = max(nums), sum(nums)

        res = r
        while l <= r:

            m = (l + r) // 2
            
            # can we split the nums arr for the sum to fit within <= m
            if can_split(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res


