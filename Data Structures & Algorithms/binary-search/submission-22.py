class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums) // 2
        print(nums)
        if len(nums) == 1 and nums[middle] != target:
            return -1
        
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            result = self.search(nums[middle:], target)
            
            if result == -1:
                return result
            else:
                return middle + result
        else:
            return self.search(nums[:middle], target)