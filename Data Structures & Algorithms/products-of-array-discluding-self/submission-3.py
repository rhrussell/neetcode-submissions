class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        # prod_nums = [2 * 4 * 6, 1 * 4 * 6, 1 * 2 * 6, 1 * 2 * 4]

        # nums = [-1, 0, 1, 2, 3]
        # prod_nums = [0 * 1 * 2 * 3, -1 * 1 * 2 * 3, -1 * 0 * 2 * 3, -1 * 0 * 1 * 3, -1 * 0 * 1 * 2]
        # prod_nums = [0, -6, 0, 0, 0]

        # nums = [0, 0]
        # prod_nums = [0, 0]

        # nums = [0, 8, 0]
        # prod_nums = [8 * 0, 0 * 0, 0 * 8]

        result = [0] * len(nums)
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        j = len(nums) - 2
        for i in range(1, len(nums), 1):
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[j] = nums[j] * postfix[j + 1]
            j -= 1
        
        for i in range(len(result)):
            if i == 0:
                result[i] = 1 * postfix[i + 1]
            elif i == len(result) - 1:
                result[i] = prefix[i - 1] * 1
            else:
                result[i] = prefix[i - 1] * postfix[i + 1]

        return result