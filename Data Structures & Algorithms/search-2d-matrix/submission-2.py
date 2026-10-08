class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            else:
                return self.binary_search(0, len(row) - 1, row, target)
        
        return False

    def binary_search(self, left: int, right: int, nums: List[int], target: int) -> bool:
        if left > right:
            return False
        
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return True
        if nums[middle] < target:
            return self.binary_search(middle + 1, right, nums, target)
        else:
            return self.binary_search(0, right - 1, nums, target)