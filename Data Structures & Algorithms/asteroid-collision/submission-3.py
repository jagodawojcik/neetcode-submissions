class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for n in asteroids:
            alive = True

            while alive and res and res[-1] > 0 and n < 0:
                if res[-1] < abs(n):
                    res.pop()
                elif res[-1] == abs(n):
                    res.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                res.append(n)

        return res
