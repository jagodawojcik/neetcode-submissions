class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        accumulator = 1
        for n in nums:
            accumulator *= n 
            prefix.append(accumulator)

        print(prefix)

        postfix = [1]
        acc_post = 1
        for n in reversed(nums):
            acc_post *= n
            postfix.append(acc_post)

        print(postfix)

        result = []
        for i, n in enumerate(nums):
            result.append(prefix[i] * postfix[len(nums) - i - 1])

        print(result)
        return result



