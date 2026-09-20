class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        len1, len2 = len(nums1), len(nums2)
        n1, n2 = 0, 0

        median1 = 0
        for i in range(((len1+len2) // 2) + 1):
            median2 = median1
            if n1 < len(nums1) and n2 < len(nums2):
                if nums1[n1] < nums2[n2]:
                    median1 = nums1[n1]
                    n1 += 1
                else:
                    median1 = nums2[n2]
                    n2 += 1
            elif n1 < len(nums1):
                median1 = nums1[n1]
                n1 += 1
            else:
                median1 = nums2[n2]
                n2 += 1

        

        if (len1 + len2) % 2 == 0:
            return (median1 + median2) / 2
        else:
            return float(median1)

