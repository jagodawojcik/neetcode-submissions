class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        postfix = [1]
        acc_post = 1
        for n in reversed(nums):
            acc_post *= n
            postfix.append(acc_post)
        

        result = []
        accumulator = 1
        for i, n in enumerate(nums):
            result.append(accumulator * postfix[len(nums) - i - 1])
            accumulator *= n 

        return result



