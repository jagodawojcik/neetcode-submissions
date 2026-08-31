class Solution:
    def sortColors(self, nums: List[int]) -> None:


        color_count = [0] * 3

        for n in nums:
            color_count[n] += 1

        i = 0
        for color, freq in enumerate(color_count):
            while freq > 0:
                nums[i] = color
                freq -= 1
                i += 1


