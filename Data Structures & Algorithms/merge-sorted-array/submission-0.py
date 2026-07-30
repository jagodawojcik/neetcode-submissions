class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        new_nums = []
        l, r = 0, 0

        while l < len(nums1) - n and r < len(nums2):
            if nums1[l] < nums2[r]:
                new_nums.append(nums1[l])
                l += 1
            else:
                new_nums.append(nums2[r])
                r += 1

        while l < len(nums1) - n:
            new_nums.append(nums1[l])
            l += 1

        while r < len(nums2):
            new_nums.append(nums2[r])
            r += 1

        nums1[:] = new_nums
