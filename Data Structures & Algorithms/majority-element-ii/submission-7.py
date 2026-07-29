class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # nums=[5,2,3,2,2,2,2,5,5,5]

        count1, count2 = 0, 0
        res1, res2 = None, None
        for n in nums:
            if n == res1:
                count1 += 1
            elif n == res2:
                count2 += 1
            elif count1 == 0:
                res1 = n
                count1 = 1
            elif count2 == 0:
                res2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        threshold = len(nums) // 3

        if nums.count(res1) > threshold:
            res.append(res1)
        if nums.count(res2) > threshold:
            res.append(res2)

        return res
            


