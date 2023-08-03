class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0

        ans = 0

        i = 1
        j = len(height)-1

        leftMax = height[0]
        rightMax = height[-1]


        while i<=j:
            if height[i] > leftMax:
                leftMax = height[i]
            if height[j] > rightMax:
                rightMax = height[j]

            if leftMax <= rightMax:
                ans += leftMax - height[i]
                i += 1
            else:
                ans += rightMax - height[j]
                j -= 1
        return ans


