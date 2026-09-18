class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, left: int, right: int, nums: List[int], target: int) -> int:
        if left > right:
            return -1
        
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            return self.binary_search(middle + 1, right, nums, target)
        else:
            return self.binary_search(0, right - 1, nums, target)