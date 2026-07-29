class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # [5,5,1,1,1,5,5]
        count = 0
        res = None
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
            # if res != n:
            #     if count > 0: 
            #         count -= 1
            #     if count == 0:
            #         res = n
            #         count += 1
            # else:
            #     count += 1
        
        return res
            


