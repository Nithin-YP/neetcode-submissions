class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        max_len = 0
        l , r = 0 , 0
        n = len(s)
        while(l<=r and l < n  and r<n):
            while(s[r] in found):
                found.remove(s[l])
                l+=1
            found.add(s[r])
            r+=1
            max_len = max(max_len , r-l)
        return max_len
