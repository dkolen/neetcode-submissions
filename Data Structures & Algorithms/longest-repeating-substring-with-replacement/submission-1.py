class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        longest = 0
        l, r = 0, 0

        while r < len(s):
            counts[s[r]] += 1
            r += 1
            highestFreq = 0
            for key in counts:
                highestFreq = max(highestFreq, counts[key])
            if highestFreq + k < (r - l):
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l)
        return longest
