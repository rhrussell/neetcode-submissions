class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break # the smallest number is positive so that means that no sum will equal 0

            if i > 0 and num == nums[i - 1]:
                continue # takes care of duplicates

            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = num + nums[j] + nums[k]

                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    result.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1 # takes care of duplicates

        return result