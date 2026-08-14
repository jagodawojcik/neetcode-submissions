class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time to reach target destination = (target - position) / speed

        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_speed.sort()

        fleets = []
        for i in pos_speed[::-1]:
            fleets.append((target - i[0]) / i[1])

            if len(fleets) >= 2 and fleets[-2] >= fleets[-1]:
                fleets.pop()
            
        return len(fleets)


