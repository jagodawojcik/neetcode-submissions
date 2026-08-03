class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        values_seen = {}

        for i in range(len(nums)):
            if nums[i] in values_seen and i - values_seen[nums[i]] <= k:
                return True
            values_seen[nums[i]] = i

        return False
