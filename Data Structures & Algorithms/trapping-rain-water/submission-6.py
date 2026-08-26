class Solution:
    def trap(self, height: List[int]) -> int:
        curr_max = 0
        area = 0

        # Initialize with the first element
        prefix = [height[0]]
        suffix = [0] * len(height)

        # Track the running maximum and append to the result
        for num in height[1:]:
            prefix.append(max(prefix[-1], num)) 

        for i in range(len(height) - 1, -1, -1):
            if height[i] > curr_max:
                curr_max = height[i]
            suffix[i] = curr_max

        for i in range(0, len(height) - 1):
            water = min(prefix[i], suffix[i]) - height[i]

            if water > 0:
                area += water

        return area
            