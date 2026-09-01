class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        result = 0

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                num_two = nums.pop()
                num_one = nums.pop()

                if token == '+':
                    result = num_one + num_two
                elif token == '-':
                    result = num_one - num_two
                elif token == '*':
                    result = num_one * num_two
                elif token == '/':
                    result = num_one / num_two

                nums.append(int(result))

            else:
                nums.append(int(token))

                if len(nums) == 1:
                    result = nums[0]

        return int(result)