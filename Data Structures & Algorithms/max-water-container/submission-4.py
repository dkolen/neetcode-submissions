class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(l, r):
            return (r - l) * min(heights[l], heights[r])
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            res = max(res, calcArea(l, r))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
        