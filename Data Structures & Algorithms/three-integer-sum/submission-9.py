class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = set()
        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0 and l < r:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0 and l < r:
                    l += 1
                else:
                    ans.add((nums[l], nums[r], nums[i]))
                    l += 1
                    r -= 1

            
        return [list(i) for i in ans]