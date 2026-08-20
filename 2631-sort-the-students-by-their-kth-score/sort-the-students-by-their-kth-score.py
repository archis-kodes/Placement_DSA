class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        value_index_map = []
        for i in range(len(score)):
            value_index_map.append((score[i][k], i))
        # Sort
        value_index_map = sorted(value_index_map, reverse = True)
        # Change Order
        n = len(score)
        for i, j in value_index_map:
            score.append(score[j])
        return score[n:]