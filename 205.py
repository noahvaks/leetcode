# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #make hash map of s values to t values 
        d = {}
        for i in range(len(s)):
            if s[i] not in d and t[i] not in d.values(): 
                d.update({s[i]:t[i]})
        #check t against hash map
        for i in range(len(s)):
            if s[i] not in d:
                return False
            elif t[i] != d[s[i]]: return False
        return True
        
