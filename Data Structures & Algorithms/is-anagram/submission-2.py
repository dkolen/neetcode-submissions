class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCtr = Counter(s)
        tCtr = Counter(t)
        return sCtr == tCtr