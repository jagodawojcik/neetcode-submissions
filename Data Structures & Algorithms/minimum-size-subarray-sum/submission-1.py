class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        l = 0
        res = float("inf")
        subarr_sum = 0

        for r in range(len(nums)):
            subarr_sum += nums[r]
            while subarr_sum >= target:
                res = min(res, (r - l + 1))
                subarr_sum -= nums[l]
                l += 1

        return 0 if res == float("inf") else res



