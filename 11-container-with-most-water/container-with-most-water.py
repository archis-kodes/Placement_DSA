class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total_vol = right * min(height[left], height[right])
        while left<right:
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
            vol = min(height[left], height[right]) * (right - left)
            total_vol = max(total_vol, vol)
        return total_vol