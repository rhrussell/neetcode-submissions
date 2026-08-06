class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        set_nums = set()

        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                result = True

        return result