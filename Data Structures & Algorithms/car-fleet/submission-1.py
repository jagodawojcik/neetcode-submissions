class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = []
        for p, s in zip(position, speed):
            pos_speed.append((p,s))  # create 'merged' list of (pos, speed)
        
        pos_speed.sort()
        fleets = []
        print(pos_speed)
        for car in pos_speed[::-1]:
            fleets.append((target - car[0]) / car[1])
            print(fleets)
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)