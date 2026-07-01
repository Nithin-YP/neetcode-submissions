class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += "".join(str(l)+"#"+s)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        len_s =""
        ind = 0
        l = len(s)
        while ind < l:
            j = ind
            while s[j] != '#':
                j +=1
            len_s = int(s[ind:j])
            word = s[j+1:j+len_s+1]
            res.append(word)
            ind = j+1+len_s
        return res
            
        
            
            