class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_one = 0
        index_two = len(numbers) - 1

        while numbers[index_one] + numbers[index_two] != target:
            if numbers[index_one] + numbers[index_two] > target:
                index_two -= 1
            elif numbers[index_one] + numbers[index_two] < target:
                index_one += 1
        
        return [index_one + 1, index_two + 1]
        