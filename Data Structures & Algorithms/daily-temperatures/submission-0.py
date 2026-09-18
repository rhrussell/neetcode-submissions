class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: [[temp, index], ...]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:    # gets the last added pair and gets the temperature from that pair
                stack_temp, stack_index = stack.pop()   # have to break up the two variables when you do a pop
                result[stack_index] = index - stack_index
            stack.append((temp, index))
        return result