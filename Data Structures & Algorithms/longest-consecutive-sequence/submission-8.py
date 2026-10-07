class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = set(nums)
        largest = 0
        for n in counts:
            if n - 1 not in counts:
                i = n
                while i + 1 in counts:
                    i += 1
                largest = max(largest, i - n + 1)
        return largest