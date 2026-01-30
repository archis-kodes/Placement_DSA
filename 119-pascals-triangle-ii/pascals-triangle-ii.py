class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(rowIndex):
            temp = [1]
            for j in range(len(prev)-1):
                temp.append(prev[j] + prev[j+1])
            temp.append(1)
            prev = temp
        return prev