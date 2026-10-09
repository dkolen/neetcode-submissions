class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = min(len(s), 1)
        while r < len(s) - 1:
            r += 1
            if s[r] in s[l:r]:
                while s[l] != s[r] and l < r:
                    l += 1
                if l < r:
                    l += 1
            longest = max(r-l+1, longest)
        return longest