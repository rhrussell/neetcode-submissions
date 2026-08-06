class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, num in enumerate(nums): # enumerate(nums) => ((0, nums[0]), (1, nums[1]), ...)
            diff = target - num
            if diff in my_dict:
                return [my_dict[diff], i] # i comes second since my_dict[diff] cause it was added in a previous iteration
            my_dict[num] = i # dont have to keep all indices of the occurences of a num just the latest one
