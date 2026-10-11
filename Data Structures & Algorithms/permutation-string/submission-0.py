class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Chars = {}
        s2Chars = {}
        for idx, c in enumerate(s1):
            s1Chars[c] = s1Chars.get(c, 0) + 1
            s2Chars[s2[idx]] = s2Chars.get(s2[idx], 0) + 1
        s1Keys = list(s1Chars.keys())
        for i in range(len(s1) - 1, len(s2) - 1):
            isPerm = True
            for key in s1Keys:
                if s1Chars[key] != s2Chars.get(key, 0):
                    isPerm = False
            if isPerm:
                return True
            s2Chars[s2[i - len(s1) + 1]] -= 1
            s2Chars[s2[i+1]] = s2Chars.get(s2[i + 1], 0) + 1
        isPerm = True
        for key in s1Keys:
            if s1Chars[key] != s2Chars.get(key, 0):
                isPerm = False
        return isPerm
            
