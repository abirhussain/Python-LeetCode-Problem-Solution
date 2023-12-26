class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sz = n+1
        curr_sum = 0
        left,right = 0, 0
        while right < n:
            curr_sum += nums[right]
            while curr_sum >= target:
                sz = min(right-left+1, sz)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return sz if sz != n+1 else 0