class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        ans = [0] * (2*len_nums)

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i+len_nums] = n
        
        return ans