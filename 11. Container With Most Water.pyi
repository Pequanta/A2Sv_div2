class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 1
        right = len(height)
        max_area = float("-inf")
        while left < len(height):
            height_g = min(height[left-1], height[right-1])
            width = right - left
            max_area = max(max_area, height_g * width)
            if height[right - 1] < height[left-1]:
                right -= 1
                continue
            left += 1
        return max_area
