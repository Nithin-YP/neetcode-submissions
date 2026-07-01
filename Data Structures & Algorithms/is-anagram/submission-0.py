class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for x in s:
            if x in d :
                d[x] += 1
            else:
                d[x] = 1
        for  x in t:
            if x in d :
                d[x] -= 1
                if d[x] == 0:
                    d.pop(x)
            else:
                return False
        if len(d) == 0:
            return True
        return False
