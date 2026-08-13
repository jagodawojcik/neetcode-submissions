class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time to reach target destination = (target - position) / speed
        
        pos_speed = [[p, s] for p, s in zip(position, speed)]
        # pos_speed = []
        # for i in range(len(position)):
        #     pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort()
        fleets = []
        for p, s in pos_speed[::-1]:
            fleets.append((target - p) / s)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()

        return len(fleets)