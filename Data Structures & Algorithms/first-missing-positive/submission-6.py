class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # res -> 1..len(n)+1 

        # [1, 2, 3]
        #  0, 1, 2

        # First pass, remove neg values [0,0,0]
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # Second pass, marking vals at inx with (-) for positive integers withing res range
        for i, n in enumerate(nums):
            val = abs(n)
            if  0 < val < len(nums) + 1:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                if nums[val-1] == 0:
                    nums[val-1] = -(len(nums) + 1)

        # Third pass: searching for solution
        res = 1
        for n in nums:
            if n >= 0:
                return res
            res += 1

        return res










        



                




        