class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res = []
        # asteroids=[-2,-1,1,2]
        for a in asteroids:
            if a > 0:
                res.append(a)
                continue

            if not res:
                res.append(a)
                continue

            alive = True
            while alive and res and res[-1] > 0:
                if res[-1] < abs(a):
                    res.pop()
                elif res[-1] == abs(a):
                    res.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                res.append(a)

        return res