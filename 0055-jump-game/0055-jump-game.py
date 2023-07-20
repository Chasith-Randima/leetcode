class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        num = 0

        for i in range(n):
            if num < i:
                return False
            num = max(num,i+nums[i])

        return True