class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res = []
        for a in asteroids:            
            alive = True
            while res and a < 0 and res[-1] > 0 and alive:
                if res[-1] > abs(a):
                    alive = False
                elif res[-1] == abs(a):
                    res.pop()
                    alive = False
                else:
                    res.pop()

            if alive:
                res.append(a)

        
        return res

