# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # map pattern to string.. should be same as last problem but with new mapping type
        s = s.split()
        if len(s) != len(pattern): return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d and s[i] not in d.values(): 
                d.update({pattern[i]:s[i]})
        for i in range(len(pattern)):
            if pattern[i] not in d: return False
            elif s[i] != d[pattern[i]]: return False
        
        return True
