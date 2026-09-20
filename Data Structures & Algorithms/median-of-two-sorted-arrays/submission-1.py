class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A


        half = (len(A) + len(B)) // 2
        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2 # A[:m+1]
            j = half - m - 2 # B[:j+1]

            # left & right of the boundary at m & j
            A_left = A[m] if m >= 0 else float('-infinity')
            A_right = A[m+1] if m + 1< len(A) else float('infinity')
            B_left = B[j] if j >= 0 else float('-infinity')
            B_right = B[j+1] if j + 1 < len(B) else float('infinity')

            # binary search
            if A_left > B_right:
                r = m - 1
            elif B_left > A_right:
                l = m + 1
            else:
                # found valid ranges, compute median
                if (len(A) + len(B)) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return float(min(A_right, B_right))


            


