class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # [-2,-1,0] -> 1
        # [0,1,2] -> 3
        # [1,2,3] -> 4 len(arr) -> len(arr) + 1

        nums_set = set(nums)

        res = 1
        i = 0
        while i < (len(nums) + 1):
            if res in nums_set:
                res += 1
            i += 1
            
        return res


        



                




        