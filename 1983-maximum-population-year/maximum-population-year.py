class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        
        for start, end in logs:
            events.append([start, 1])
            events.append([end, -1])

        events.sort()

        population = 0
        max_year = 0
        max_population = 0

        for year, status in events:

            population += status
            
            if population > max_population:
                max_population = population
                max_year = year

        return max_year