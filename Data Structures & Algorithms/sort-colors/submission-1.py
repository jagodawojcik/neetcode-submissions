class Solution:
    def sortColors(self, nums: List[int]) -> None:

        freq_color = [0] * 3

        for n in nums:
            freq_color[n] += 1
        
        i = 0
        for colour, count in enumerate(freq_color):
            for j in range(count):
                nums[i+j] = colour
            i += count
            