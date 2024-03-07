class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                Height = heights[stack.pop()]
                Width = i if not stack else i - stack[-1] -1
                max_area = max(max_area, Height * Width)
            stack.append(i)
        return max_area
        