class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min w = max(weights), max w = if days = 1, then sum(weights)
        
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            days_spent = 1
            min_w = (l + r) // 2
            capacity = min_w
            for w in weights:
                if capacity - w < 0:
                    days_spent += 1
                    capacity = min_w
                capacity -= w

            if days_spent <= days:
                r = min_w - 1
                res = min(min_w, res)
            else:
                l = min_w + 1

        return res
            





