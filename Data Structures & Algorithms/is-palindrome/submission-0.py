class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        validChars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        i,j = 0, len(s) - 1
        while i < j:
            bothValid = True
            if s[i] not in validChars:
                i+=1
                bothValid = False
            if s[j] not in validChars:
                j-=1
                bothValid = False
            if bothValid:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True
            
        