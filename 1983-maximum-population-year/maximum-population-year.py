class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        n = len(logs)
        for i in range(n):
            logs[len(logs):len(logs)] = ([logs[i][0], 1], [logs[i][1], -1])
        logs[0:n] = []
        print(logs)
        
        logs.sort()

        max_population = 0
        max_year = logs[0][0]
        population = 0
        for i in range(len(logs)):
            population += logs[i][1]
            if population > max_population:
                max_population = population
                max_year = logs[i][0]
        return max_year