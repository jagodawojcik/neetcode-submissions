class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for n in asteroids:
            alive = True

            while alive and res and res[-1] > 0 and n < 0:
                if res[-1] < abs(n):
                    res.pop() # remove smaller positive val from top, n stays alive
                elif res[-1] == abs(n):
                    res.pop() # equal, val from top removed, n removed too
                    alive = False
                else:
                    alive = False # n is smaller, remove

            if alive:
                res.append(n)

        return res
