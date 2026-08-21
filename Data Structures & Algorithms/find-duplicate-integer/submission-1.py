class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0 # index

        # nums = [1,2,3,2,2]
        # inx  = [0,1,2,3,4]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # fast and slow from prev loop, they are equal dist from the `start cycle` n
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


        