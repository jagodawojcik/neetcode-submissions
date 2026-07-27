class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # 1st pass: replace all negative values with zeros, we don't care
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0

        # 2nd pass: mark val under the index as negative to show presence of integer
        for i, n in enumerate(nums):
            val = abs(n)
            if 0 < val < len(nums) + 1:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                if nums[val - 1] == 0:
                    nums[val - 1] = -(len(nums) + 1)

        # 3rd pass: find smallest positive integer
        for i, n in enumerate(nums):
            if n >= 0:
                return i + 1

        return len(nums) + 1


        

                




        