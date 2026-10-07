class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(l, r, lVal, rVal):
            return (r - l) * min(lVal, rVal)
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            lVal = heights[l]
            rVal = heights[r]
            res = max(res, calcArea(l, r, lVal, rVal))
            if lVal <= rVal:
                l += 1
                while heights[l] < lVal:
                    l += 1
            else:
                r -= 1
                while heights[r] < rVal:
                    r -= 1
        return res
        