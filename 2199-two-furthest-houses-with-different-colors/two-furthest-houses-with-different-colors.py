class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxDist = []
        for left in range(len(colors)):
            right = len(colors)-1
            while left<right:
                if colors[left]!=colors[right]:
                    maxDist.append(right-left)
                    break
                right-=1
        return max(maxDist)