class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        my_dict = {}

        for index, num in enumerate(nums):
            my_dict[num] = index

        for index, num in enumerate(nums):
            if (target - num) in my_dict and index != my_dict.get(target - num):
                result.append(index)
                result.append(my_dict.get(target - num))
                break

        return result