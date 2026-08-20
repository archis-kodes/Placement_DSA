class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_map = []
        for i in range(len(heights)):
            height_map.append((names[i], heights[i]))

        # Sort in descending order
        height_map = sorted(height_map, key = lambda item: item[1], reverse=True)

        #result
        result = []
        for i in height_map:
            result.append(i[0])
        return result
