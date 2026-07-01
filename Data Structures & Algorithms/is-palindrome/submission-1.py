class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for c in s:
            ch = c.lower()
            if(ch.isalnum()):
                clean_s += ch
        n = len(clean_s)
        for i in range(n//2):
            if(clean_s[i] != clean_s[n-i-1]):
                return False
        return True