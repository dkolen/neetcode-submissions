class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freqs = [[] for i in range(len(nums))]
        res = []
        for num in nums:
            counts[num] += 1
        for num in counts:
            freqs[counts[num]-1].append(num)
        for i in range(len(freqs) - 1, -1, -1):
            while freqs[i]:
                res.append(freqs[i].pop())
                if len(res) == k:
                    return res
        