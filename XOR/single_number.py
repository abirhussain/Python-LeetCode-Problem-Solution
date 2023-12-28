class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_number = nums[0]
        for i in range(1,len(nums)):
            unique_number = unique_number ^ nums[i]
        return unique_number
        