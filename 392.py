# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        #go through the big loop
        for i in range(len(t)):
            #increment up if matching (while <= smaller one?)
            if j < len(s):
                if t[i] == s[j]:
                    j+=1
        if j == len(s):
            return True
        return False
        
        
        
