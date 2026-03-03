class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        L = []
        for log in logs:
            L.append([log[0], 1])
            L.append([log[1], -1])
        L.sort()
        print(L)
        # Find Max
        max_year = L[1][0]
        maximum = 0
        add = 0
        for i in L:
            add += i[1]
            if add>maximum:
                maximum = add
                max_year = i[0]
        return max_year