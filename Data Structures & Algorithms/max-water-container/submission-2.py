class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights) -1

        max_area = 0

        while left < right:
            max_area = max(min(heights[left], heights[right]) * (right-left), max_area)

            if heights[right] <= heights[left]:
                right -=1

            elif heights[right] > heights[left]:
                left += 1

        return max_area

