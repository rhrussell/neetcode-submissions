class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index1 = 0
        index2 = len(heights) - 1
        area = 0

        while index1 != index2:
            area = max(area, (index2 - index1) * min(heights[index1], heights[index2]))

            if min(heights[index1], heights[index2]) == heights[index1]:
                index1 += 1
            else:
                index2 -= 1
        
        return area