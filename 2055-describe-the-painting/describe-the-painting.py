class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = dict()

        for start, end, color in segments:
            if start not in events:
                events[start] = color
            else:
                events[start] += color
            if end not in events:
                events[end] = -1*color
            else:
                events[end] += -1*color

        events = sorted(events.items())

        colors_array = []
        cumSum = 0
        for i in range(len(events)-1):
            cumSum += events[i][1]
            if cumSum == 0:
                continue
            colors_array.append([events[i][0], events[i+1][0], cumSum])
        return colors_array