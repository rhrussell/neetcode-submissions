class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = (end - start) * min(heights[start], heights[end]) where start and end are the two pointers in the list
        
        start = 0
        end = len(heights) - 1
        result = 0

        while start < end:
            area = (end - start) * min(heights[start], heights[end])
            result = max(result, area)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return result