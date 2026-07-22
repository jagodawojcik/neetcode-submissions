class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        num_zeros = 0
        total_product = 1
        for n in nums:
            if n == 0:
                num_zeros += 1
                continue
            total_product *= n
        
        new_arr = []
        if num_zeros >= 2:
            return [0] * len(nums)

        for n in nums:
            if n == 0:
                new_arr.append(total_product)
            else:
                if num_zeros == 1:
                    new_arr.append(0)
                else:
                    new_arr.append(int(total_product/n))
        
        return new_arr