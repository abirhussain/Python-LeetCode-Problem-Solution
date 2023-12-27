class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solution = [0]*n
        left, right = 0, n-1

        while left <= right:
            if nums[left]*nums[left]<nums[right]*nums[right]:
                solution[n-1] = nums[right]*nums[right]
                right -= 1
            else:
                solution[n-1] = nums[left]*nums[left]
                left += 1
            n -= 1

        return solution
        