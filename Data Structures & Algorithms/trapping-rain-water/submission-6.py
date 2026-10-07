class Solution:
    def trap(self, height: List[int]) -> int:
        maxPrefix = [0] * len(height)
        maxSuffix = [0] * len(height)
        res = 0
        for i in range(0, len(height) - 1):
            maxPrefix[i + 1] = max(maxPrefix[i], height[i])
            maxSuffix[-i -2] = max(maxSuffix[-i - 1], height[-i-1])
        
        for i in range(0, len(height)):
            res += max(min(maxPrefix[i], maxSuffix[i]) - height[i], 0)
        return res