class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq = [0] * 3 # index: color, val: count
        for n in nums:
            freq[n] += 1

        index = 0
        for colour, count in enumerate(freq):
            for i in range(count):
                nums[index + i] = colour
            index += count


        return nums
            