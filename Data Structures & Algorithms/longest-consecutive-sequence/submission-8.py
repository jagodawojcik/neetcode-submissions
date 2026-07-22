class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        max_seq = 1
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        counter = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                counter += 1
                if counter > max_seq:
                    max_seq = counter
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                counter = 1

        return max_seq



            