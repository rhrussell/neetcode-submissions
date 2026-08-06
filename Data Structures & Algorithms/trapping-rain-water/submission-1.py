class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        
        if length == 0:
            return 0

        prefix = [0] * len(height)
        suffix = [0] * len(height)
        area = 0

        prefix[0] = height[0]
        suffix[length - 1] = height[length - 1]

        for i in range(1, length, 1):
            prefix[i] = max(prefix[i - 1], height[i])

        for j in range(length - 2, -1, -1):
            suffix[j] = max(suffix[j + 1], height[j])

        for k in range(0, length):
            area += min(prefix[k], suffix[k]) - height[k]

        return area