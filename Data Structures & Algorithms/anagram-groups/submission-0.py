class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s1, s2):
            if len(s1) != len(s2):
                return False
            return Counter(s1) == Counter(s2)
        res = []
        for s in strs:
            added = False
            for anas in res:
                if not added and isAnagram(anas[0], s):
                    anas.append(s)
                    added = True
            if not added:
                res.append([s])
        return res
            