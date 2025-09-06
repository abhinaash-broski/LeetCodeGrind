class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range (0, len(nums)): 
            for j in range (i, len(nums)): 
                sum = nums[i]+nums[j]
                if sum == target:
                    return nums[i], nums[j]
        return []

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15, 3,4,7,23,6,3]
target=6
print(solution.twoSum(nums,target))