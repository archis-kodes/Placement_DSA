class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        number_of_bulbs = max(brightness//3, (brightness+1)//3, (brightness+2)//3)  # Ceil Value

        # Create Memory
        memory = []
        for interval in intervals:
            memory.append((interval[0], 1))
            memory.append((interval[1]+1, -1))
        memory.sort()

        # Create the time chart
        prev = 0
        prevStatus = 0
        count = 0
        for i in memory:
            if prevStatus !=0:
                count += (i[0] - prev)
            prev = i[0]
            prevStatus += i[1]


            
        return count * number_of_bulbs