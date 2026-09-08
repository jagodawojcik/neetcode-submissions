class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {} # key: difference = target - num, val: inx

        for i, n in enumerate(nums):
            if n in diff:
                return [diff[n], i]
            
            diff[target - n] = i


        return []