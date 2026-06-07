class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        # Find Minimum BULB
        minimum_bulb = (brightness+2)//3
        
        # Line Sweep
        memory = []
        for interval in intervals:
            memory.append((interval[0], 1))
            memory.append((interval[1] +1 , -1))

        memory.sort()

        prevPlace = 0
        prevStatus = 0
        total = 0
        for i in memory:
            if prevStatus!=0:
                total += i[0] - prevPlace
            prevPlace = i[0]
            prevStatus += i[1]
        return total*minimum_bulb