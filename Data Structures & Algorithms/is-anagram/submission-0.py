class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCtr = Counter(s)
        tCtr = Counter(t)
        return sCtr == tCtr