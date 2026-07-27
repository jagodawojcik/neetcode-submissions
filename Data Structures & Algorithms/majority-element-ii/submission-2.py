class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 2:
            return nums
        nums.sort() # nlog(n)

        res = set()
        freq_threshold = len(nums) // 3

        # O(n)
        freq_counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                freq_counter = 0
            
            freq_counter += 1
            if freq_counter > freq_threshold:
                res.add(nums[i])
                if len(res) >= 2:
                    return list(res)

        return list(res)


