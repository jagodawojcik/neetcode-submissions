class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #  [1,2,4,6]
        #[1,1,2,8,48] 
        #  [48,24,6,1]

        left_side = [1]
        right_side = [1]

        for i, n in enumerate(nums):
            left_side.append(n * left_side[-1])
            right_side.append(nums[-(1+i)] * right_side[-1])

        print(left_side)
        print(right_side)

        res = []
        for i in range(len(nums)):
            res.append(left_side[i] * right_side[-(2+i)])

        return res





