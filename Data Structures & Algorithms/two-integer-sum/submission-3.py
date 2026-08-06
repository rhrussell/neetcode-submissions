class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in my_dict and index != my_dict[diff]:
                return [my_dict[diff], index]
            my_dict[num] = index

        return result