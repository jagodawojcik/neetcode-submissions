class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # len(piles) <= h - always, because 1 pile per h max
        # min k = 1, max k = max in piles
        
        l, r = 1, max(piles)
        min_rate = r
        while l <= r:
            rate = (l + r) // 2
            h_spent = 0
            eaten = True
            for p in piles:
                h_spent += math.ceil(p / rate)

                if h_spent > h:
                    l = rate + 1
                    eaten = False
                    break
            if eaten:
                r = rate - 1
                min_rate = min(rate, min_rate)

        return min_rate



