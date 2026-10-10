class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[i- len(chars)])
            chars.add(s[i])
            longest = max(longest, len(chars))
        return longest
