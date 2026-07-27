class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 2:
            return nums
        nums.sort() # nlog(n)

        res = set()
        freq_threshold = len(nums) // 3

        # O(n)
        freq_counter = 0
        for i in range(0, len(nums)):
            freq_counter += 1
            
            if freq_counter > freq_threshold:
                res.add(nums[i])
                if len(res) >= 2:
                    return list(res)

            if i < len(nums) - 1 and nums[i] != nums[i+1]:
                freq_counter = 0

        return list(res)


