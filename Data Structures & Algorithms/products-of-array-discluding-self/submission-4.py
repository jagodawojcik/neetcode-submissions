class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        right_prod = []

        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]

        left_prod = [1]
        for i in range(len(nums) - 1):
            left_prod.append(left_prod[-1] * nums[i])

        print(left_prod)
        
        right_prod = [1]
        for i in range(len(nums) - 1, 0, -1):
            right_prod.append(right_prod[-1] * nums[i])

        print(right_prod)

        result = []
        for i in range(len(left_prod)): # 0, 1, 2, 3
            result.append(left_prod[i] * right_prod[-(i+1)])


        return result