class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in num_set:
            if num - 1 not in num_set:
                temp = 1
                while num + 1 in num_set:
                    temp += 1
                    num += 1
                if temp > result:
                    result = temp

        return result