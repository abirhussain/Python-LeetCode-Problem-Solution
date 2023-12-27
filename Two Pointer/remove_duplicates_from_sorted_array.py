class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, n = 0, 1, len(nums)
        while right < n:
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left+1