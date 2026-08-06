class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for num in nums:
            my_dict[str(num)] = 0

        for num in nums:
            my_dict[str(num)] += 1
            
            if my_dict[str(num)] > 1:
                return True

        return False