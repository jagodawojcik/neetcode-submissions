class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(array: List[int]) -> None:

            if len(array) <= 1:
                return

            left_array = array[:len(array)//2]
            right_array = array[len(array)//2:]

            merge_sort(left_array)
            merge_sort(right_array)

            # merge
            i, j, k = 0, 0, 0

            while j < len(left_array) and k < len(right_array):
                if left_array[j] < right_array[k]:
                    array[i] = left_array[j]
                    j += 1
                else:
                    array[i] = right_array[k]
                    k += 1
                i += 1
            
            while j < len(left_array):
                array[i] = left_array[j]
                j += 1
                i += 1

            while k < len(right_array):
                array[i] = right_array[k]
                k += 1
                i += 1

        merge_sort(nums)
        return nums
            


